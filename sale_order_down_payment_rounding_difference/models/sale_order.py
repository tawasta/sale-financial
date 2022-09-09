from odoo import models
from odoo import _


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super()._create_invoices(grouped, final, date)

        for invoice in res:
            if abs(invoice.amount_total) == 0.01:
                # We (most likely) have rounding difference of one cent.
                # Compensate this by adding a line for the rounding difference

                # Use deposit product defaults for rounding difference product
                advance = self.env["sale.advance.payment.inv"]
                product = advance._default_product_id()

                line_values = {
                    "move_id": invoice.id,
                    "name": _("Rounding difference"),
                    "quantity": 1,
                    "price_unit": invoice.amount_total * -1,
                    "product_id": product.id,
                    "product_uom_id": product.uom_id.id,
                    "tax_ids": [(6, 0, advance._default_deposit_taxes_id().ids)],
                    "account_id": product._get_product_accounts()["income"].id,
                }

                self.env["account.move.line"].with_context(
                    check_move_validity=False
                ).create(line_values)

        return res
