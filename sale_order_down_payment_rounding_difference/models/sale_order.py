from odoo import models
from odoo import _


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def _finalize_invoices(self, invoices, references):
        for invoice in invoices.values():
            invoice.compute_taxes()
            if abs(invoice.amount_total) == 0.01:
                # We (most likely) have rounding difference of one cent.
                # Compensate this by adding a line for the rounding difference

                # Use deposit product defaults for rounding difference product
                advance = self.env["sale.advance.payment.inv"]
                product = advance._default_product_id()

                line_values = {
                    'invoice_id': invoice.id,
                    'name': _("Rounding difference"),
                    'price_unit': invoice.amount_total * -1,
                    'product_id': product.id,
                    'invoice_line_tax_ids': [(6, 0, advance._default_deposit_taxes_id().ids)],
                    'account_id': product.property_account_creditor_price_difference.id,
                }

                self.env["account.invoice.line"].create(line_values)

        return super()._finalize_invoices(invoices, references)