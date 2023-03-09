from odoo import models, fields


class Currency(models.Model):
    _inherit = "res.currency"

    sale_order_rounding = fields.Boolean(
        "Sale order rounding",
        help="Round sale order totals to a whole number"
    )
