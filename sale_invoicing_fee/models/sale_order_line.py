from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    is_payment_method_fee_line = fields.Boolean(
        string="Is a payment method fee line",
        copy=False,
        help=(
            "Technical flag marking a line as an automatically added "
            "payment method fee, so it can be safely replaced/removed "
            "when the customer picks a different payment method."
        ),
    )
