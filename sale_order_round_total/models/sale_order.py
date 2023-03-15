from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for record in self:
            if (
                record.currency_id.sale_order_rounding
                and not record.amount_total.is_integer()
            ):
                # Total is not a whole number. Add a line for rounding difference
                # If rounding down, add a negative price. E.g. 10.35€ -> -0.35€
                # If rounding up, add a positive price. E.g. 10.55€ -> +0.45€
                amount = record.amount_total % 1
                if amount >= 0.5:
                    amount = 1 - amount
                else:
                    amount *= -1

                product = record.currency_id.sale_order_rounding_product_id
                tax_ids = product.taxes_id

                # If the deposit product has taxes, add taxes to the line
                tax_amount = sum(tax_ids.mapped("amount")) / 100

                if tax_amount >= 0:
                    amount = amount / (1 + tax_amount)

                line_values = {
                    "order_id": record.id,
                    "product_id": product.id,
                    "name": product.display_name,
                    "product_uom_qty": 1,
                    "price_unit": amount,
                    "product_uom": product.uom_id.id,
                    "tax_id": [(6, 0, tax_ids.ids)],
                }
                self.env["sale.order.line"].create(line_values)

        return super().action_confirm()

    def action_draft(self):
        for record in self:
            product = record.currency_id.sale_order_rounding_product_id
            # Delete rounding lines when SO is reset to draft,
            # to prevent creating multiple rounding lines
            rounding_line = record.order_line.filtered(
                lambda l: l.product_id == product and abs(l.price_unit) < 1
            )

            if rounding_line:
                rounding_line.unlink()

        return super().action_draft()
