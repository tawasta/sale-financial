from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    payment_method_id = fields.Many2one(
        comodel_name="payment.method",
        string="Selected Payment Method",
        compute="_compute_payment_method_id",
        store=True,
        readonly=False,
        precompute=True,
        help=(
            "The online payment method used (or about to be used) for this "
            "order. Drives the invoicing fee line below, if that payment "
            "method has an extra fee product configured. Defaults from the "
            "customer's 'Usual Payment Method', but the webshop checkout "
            "always overrides it with the method actually selected.\n"
            "Not to be confused with 'Payment Method' under Invoicing, "
            "which is the customer's default accounting payment method "
            "line and is unrelated to this."
        ),
    )

    @api.depends("partner_id")
    def _compute_payment_method_id(self):
        for order in self:
            order.payment_method_id = order.partner_id.payment_method_id

    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        orders._sync_payment_method_fee_line()
        return orders

    def write(self, vals):
        res = super().write(vals)
        if "payment_method_id" in vals:
            self._sync_payment_method_fee_line()
        return res

    def _sync_payment_method_fee_line(self):
        """
        Ensure each order's fee line matches its payment_method_id,
        removing any stale fee line left over from a previously selected
        payment method. Idempotent and safe to call repeatedly.
        """
        SaleOrderLine = self.env["sale.order.line"].sudo()

        for order in self:
            stale_lines = order.order_line.filtered("is_payment_method_fee_line")
            product = order.payment_method_id.product_id

            if stale_lines and product not in stale_lines.product_id:
                stale_lines.unlink()
                stale_lines = self.env["sale.order.line"]

            if not product or product in stale_lines.product_id:
                continue

            SaleOrderLine.create(
                {
                    "order_id": order.id,
                    "company_id": order.company_id.id,
                    "product_id": product.id,
                    "product_uom_qty": 1,
                    "price_unit": product.list_price,
                    "name": product.name,
                    "is_payment_method_fee_line": True,
                }
            )
