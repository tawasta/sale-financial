from odoo import fields, models


class SaleReport(models.Model):

    _inherit = "sale.report"

    commitment_date = fields.Datetime(string="Commitment Date", readonly=True)
    # pylint: disable=W0102 noqa
    def _query(self, with_clause="", fields={}, groupby="", from_clause=""):  # noqa
        fields["commitment_date"] = ", s.commitment_date as commitment_date"
        groupby += ", s.commitment_date"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
