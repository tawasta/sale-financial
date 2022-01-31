from odoo import fields, models


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    sale_order_id = fields.Many2one(
        comodel_name="sale.order",
        string="Sale Order",
        help="The Sale Order this Purchase originated from",
        copy=False,
    )

    so_client_order_ref = fields.Char(
        related="sale_order_id.client_order_ref", string="Sale Order Customer Reference"
    )

    so_partner_id = fields.Many2one(
        related="sale_order_id.partner_id", string="Sale Order Customer"
    )

    def button_confirm(self):
        res = super().button_confirm()

        for record in self:
            if record.picking_type_id.default_location_dest_id.usage != "customer":
                # Custom picking logic only for dropship-order
                continue
            sale_orders = record.order_line.mapped("sale_order_id")

            for sale_order in sale_orders:
                # Cancel the related deliveries on SO
                sale_order.picking_ids.action_cancel()

                # Change the procurement group on SO
                sale_order.procurement_group_id = record.group_id

            if len(sale_orders) == 1:
                # Set pickings sale id as current sale id
                record.picking_ids.write({"sale_id": sale_orders[0].id})

        return res
