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
        res = super().create(values)
        if "analytic_tag_ids" not in values:
            res.sudo().onchange_product_id_update_analytic_tags()

        return res

    def write(self, values):
        # This might cause problems when user tries to remove all analytic tags
        # The reason for this override is, that e-commerce orders will not, for some reason,
        # preserve analytic tags. They are set on create, but overwritten.
        if "analytic_tag_ids" not in values:
            for record in self:
                if not record.analytic_tag_ids:
                    record.sudo().onchange_product_id_update_analytic_tags()

        return super().write(values)
