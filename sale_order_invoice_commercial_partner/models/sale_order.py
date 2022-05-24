from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        if self.partner_invoice_id != self.partner_invoice_id.commercial_partner_id:
            res["partner_id"] = self.partner_invoice_id.commercial_partner_id.id
