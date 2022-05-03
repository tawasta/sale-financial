from odoo import _, fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    sale_to_purchase_note_text = fields.Text(translate=True,
        default=lambda self: self._default_sale_to_purchase_note_text())

    def _default_sale_to_purchase_note_text(self):
        text = _("Please print this customer reference to your delivery note:")
        return text
