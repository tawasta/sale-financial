
from odoo import api, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('analytic_account_id')
    def onchange_analytic_account_id_update_analytic_tags(self):
        for record in self:
            if (record.analytic_account_id and
                    record.analytic_account_id.project_ids
                    and record.analytic_account_id.project_ids[0].analytic_tag_ids):
                for line in record.order_line:
                    line.analytic_tag_ids += \
                        record.analytic_account_id.project_ids[0].analytic_tag_ids
