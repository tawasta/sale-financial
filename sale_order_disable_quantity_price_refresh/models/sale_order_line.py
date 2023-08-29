from odoo import api, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    @api.onchange("product_uom", "product_uom_qty")
    def product_uom_change(self):
        # Don't auto-update anything when quantity is changed
        if self._context.get("quantity"):
            return

        return super(SaleOrderLine, self).product_uom_change()
