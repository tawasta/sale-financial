from odoo import fields, models


class Currency(models.Model):
    _inherit = "res.currency"

    sale_order_rounding = fields.Boolean(
        "Sale order rounding", help="Round sale order totals to a whole number"
    )

    sale_order_rounding_product_id = fields.Many2one(
        string="Rounding product",
        comodel_name="product.product",
        help="The product to use for rounding. Defaults to deposit product",
    )
