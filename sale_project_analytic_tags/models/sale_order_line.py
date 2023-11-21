from odoo import fields, models


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    analytic_tag_ids = fields.Many2many(
        default=lambda self: self._default_get_analytic_tag_ids()
    )

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
