from odoo import fields, models


class PaymentMethod(models.Model):
    _inherit = "payment.method"

    product_id = fields.Many2one(
        string="Extra fee product",
        comodel_name="product.product",
        help=(
            "When set, this product is added as a line to the sale order "
            "when a customer pays with this payment method."
        ),
    )
