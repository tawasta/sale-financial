from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    payment_method_id = fields.Many2one(
        comodel_name="payment.method",
        string="Usual Payment Method",
        help=(
            "The online payment method this customer usually pays with. "
            "Used only as the default for new sale orders' 'Selected "
            "Payment Method' field; each order can still be set to a "
            "different payment method."
        ),
    )
