from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)


class SaleReport(models.Model):
    _inherit = "sale.report"

    commitment_date = fields.Datetime(string="Commitment Date", readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res["commitment_date"] = "s.commitment_date"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            s.commitment_date"""
        return res
