from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _check_line_unlink(self):
        """Bypass unlink check on a rounding product"""

        # lines is a set of order lines that cannot be deleted
        lines = super()._check_line_unlink()

        product = self.order_id.currency_id.sale_order_rounding_product_id

        # Filter a rounding product out, which allows deleting it
        return lines.filtered(lambda l: l.product_id != product)
