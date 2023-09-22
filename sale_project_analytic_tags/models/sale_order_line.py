
from odoo import fields, models


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    analytic_tag_ids = fields.Many2many(
        default=lambda self: self._default_get_analytic_tag_ids()
    )

    def _default_get_analytic_tag_ids(self):
        res = False

        analytic_account_id = self._context.get('analytic_account_id')
        if analytic_account_id:
            analytic_account = self.env['account.analytic.account'].\
                browse([analytic_account_id])

            res = analytic_account and analytic_account.project_ids and \
                analytic_account.project_ids[0].analytic_tag_ids

        return res
