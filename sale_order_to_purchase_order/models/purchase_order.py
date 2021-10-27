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
