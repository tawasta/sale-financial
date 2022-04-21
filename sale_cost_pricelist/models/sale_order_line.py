from odoo import api
from odoo import fields
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("product_id", "company_id", "currency_id", "product_uom")
    def _compute_purchase_price(self):
        res = super()._compute_purchase_price()

        for record in self:
            product = record.product_id

            if (
                not product
                or not record.purchase_price
                or not record.order_id.purchase_pricelist_id
            ):
                continue

            # Recompute the price using cost pricelist
            price = record.purchase_price
            pricelist = record.order_id.purchase_pricelist_id
            uom = record.product_uom
            quantity = record.product_uom_qty
            partner = record.order_id.partner_id
            date_order = record.order_id.date_order.date()

            rule = pricelist._compute_price_rule(
                [(product, quantity, partner)], date_order, uom.id
            )
            if rule.get(product.id):
                rule_id = rule[product.id][1]
                pricelist_item = self.env["product.pricelist.item"].browse([rule_id])

                purchase_price = pricelist_item._compute_price(
                    price, uom, product, quantity, partner
                )
                if purchase_price:
                    record.purchase_price = purchase_price

        return res
