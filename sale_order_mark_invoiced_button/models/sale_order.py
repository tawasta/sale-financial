from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def action_mark_invoiced(self):
        for record in self:
            record.force_invoiced = True
