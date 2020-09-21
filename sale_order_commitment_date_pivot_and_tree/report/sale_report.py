from odoo import fields, models


class SaleReport(models.Model):

    _inherit = 'sale.report'

    commitment_date = fields.Datetime(string='Commitment_date', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['commitment_date'] = ", s.commitment_date as commitment_date"
        groupby += ', s.commitment_date'
        return super(SaleReport, self)._query(
            with_clause, fields, groupby, from_clause
        )
