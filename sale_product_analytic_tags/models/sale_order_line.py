from odoo import api, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    @api.onchange("product_id")
    def onchange_product_id_update_analytic_tags(self):
        for record in self:
            if record.product_id and record.product_id.get_analytic_tags():
                record.analytic_tag_ids += record.product_id.get_analytic_tags()

    @api.model
    def create(self, values):

        if "analytic_tag_ids" not in values:
            product_id = values.get("product_id")
            product = self.env["product.product"].browse([product_id])

            values["analytic_tag_ids"] = [(6, 0, product.get_analytic_tags().ids)]

        return super(SaleOrderLine, self).create(values)
