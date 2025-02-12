from odoo import fields, models


class SaleToPurchaseWizard(models.TransientModel):
    _name = "sale.to.purchase.wizard"

    def create_purchase(self, current_sale):
        purchase_order_model = self.env["purchase.order"]

        initial_values = {
            "partner_id": self.partner_id.id,
            "company_id": current_sale.company_id.id,
            "currency_id": current_sale.currency_id.id
            or self.env.company.currency_id.id,
            "picking_type_id": self.picking_type_id.id,
            "origin": current_sale.name,
            "payment_term_id": self.partner_id.property_supplier_payment_term_id.id,
            "sale_order_id": current_sale.id,
        }

        if self.picking_type_id.default_location_dest_id.usage == "customer":
            # Dropshipping
            initial_values["dest_address_id"] = current_sale.partner_shipping_id.id

            if current_sale.client_order_ref:
                initial_values["notes"] = "{} {}".format(
                    current_sale.company_id.with_context(
                        lang=self.partner_id.lang
                    ).sale_to_purchase_note_text,
                    current_sale.client_order_ref,
                )

        updated_values = purchase_order_model.play_onchanges(
            initial_values, ["partner_id"]
        )

        return purchase_order_model.create(updated_values)

    def create_purchase_line(self, current_sale_line, purchase_order):
        purchase_order_line_model = self.env["purchase.order.line"]

        initial_values = {
            "order_id": purchase_order.id,
            "product_id": current_sale_line.product_id.id,
            "product_qty": current_sale_line.product_uom_qty,
            "product_uom": current_sale_line.product_uom.id,
            "partner_id": purchase_order.partner_id.id,
            "sale_order_id": current_sale_line.order_id.id,
            "sale_line_id": current_sale_line.id,
        }

        order_line = purchase_order_line_model.create(initial_values)
        order_line._compute_price_unit_and_date_planned_and_name()

        return order_line

    def button_create_po(self):
        current_sale = self.env["sale.order"].browse(self.env.context["active_id"])
        po_res = self.create_purchase(current_sale)

        for so_line in current_sale.order_line:
            self.create_purchase_line(so_line, po_res)

        return {
            "view_type": "form",
            "view_mode": "form",
            "res_model": "purchase.order",
            "type": "ir.actions.act_window",
            "res_id": po_res.id,
            "context": self.env.context,
        }

    def _get_default_picking_type(self):
        args = [
            ("code", "=", "incoming"),
            ("warehouse_id", "=", self.env.context["warehouse_id"]),
        ]

        res = self.env["stock.picking.type"].search(args, limit=1)
        return res and res[0] or False

    def _get_default_customer(self):
        return self.env.context.get("customer_id", False)

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Supplier",
        domain=[("supplier_rank", ">", 0)],
        required=True,
    )

    customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        readonly=True,
        default=_get_default_customer,
    )

    picking_type_id = fields.Many2one(
        comodel_name="stock.picking.type",
        string="Delivery Location",
        required=True,
        default=_get_default_picking_type,
    )
