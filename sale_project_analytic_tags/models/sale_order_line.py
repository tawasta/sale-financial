from odoo import models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    def _compute_analytic_tag_ids(self):
        # First default analytic tags
        super()._compute_analytic_tag_ids()
        for record in self:
            analytic_account = record.order_id.analytic_account_id
            # Add project-specific tags
            if (
                analytic_account.project_ids
                and analytic_account.project_ids[0].analytic_tag_ids
            ):
                record.analytic_tag_ids += analytic_account.project_ids[
                    0
                ].analytic_tag_ids
