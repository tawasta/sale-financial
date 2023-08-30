from odoo import api, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    @api.depends("price_subtotal", "product_uom_qty", "purchase_price")
    def _compute_margin(self):
        super(SaleOrderLine, self)._compute_margin()

        for line in self:
            if line.product_id.margin_ignore:
                line.margin = 0
                line.margin_percent = 0
