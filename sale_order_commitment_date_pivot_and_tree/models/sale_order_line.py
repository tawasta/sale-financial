from odoo import fields, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    commitment_date = fields.Datetime(related="order_id.commitment_date")
