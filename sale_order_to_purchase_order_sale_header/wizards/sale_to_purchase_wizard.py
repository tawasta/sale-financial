from odoo import models


class SaleToPurchaseWizard(models.TransientModel):
    _inherit = "sale.to.purchase.wizard"

    def create_purchase(self, current_sale):
        res = super().create_purchase(current_sale)
        res.header_text = current_sale.header_text
        return res
