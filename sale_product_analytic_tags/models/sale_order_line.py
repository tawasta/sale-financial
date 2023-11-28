from odoo import api, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    def _compute_analytic_tag_ids(self):
        # First default analytic tags
        super()._compute_analytic_tag_ids()
        for record in self:
            if not record.display_type and record.state == "draft":
                # Add product-specific tags
                if record.product_id and record.product_id.get_analytic_tags():
                    record.analytic_tag_ids += record.product_id.get_analytic_tags()

    @api.model
    def create(self, values):

        if "analytic_tag_ids" not in values:
            product_id = values.get("product_id")
            product = self.env["product.product"].browse([product_id])

            values["analytic_tag_ids"] = [(6, 0, product.get_analytic_tags().ids)]

        return super().create(values)
