from odoo import fields
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    purchase_pricelist_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Cost pricelist",
        readonly=True,
        states={"draft": [("readonly", False)], "sent": [("readonly", False)]},
    )

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)

        if self.product_id and self.order_id.purchase_pricelist_id:
            price = self.product_id.purchase_price
            pricelist = self.order_id.purchase_pricelist_id
            product = self.product_id
            uom = self.uom_id
            quantity = self.quantity
            partner = self.order_id.partner_id
            date_order = self.order_id.date_order.date()

            rule = pricelist._compute_price_rule(
                [(product, quantity, partner)], date_order, uom.id
            )
            if rule.get(product.id):
                rule_id = rule[product.id][1]
                pricelist_item = self.env["product.pricelist.item"].browse([rule_id])

                res["purchase_price"] = pricelist_item._compute_price(
                    price, uom, product, quantity, partner
                )
                print("HERE")
                print(res["purchase_price"])

        return res
