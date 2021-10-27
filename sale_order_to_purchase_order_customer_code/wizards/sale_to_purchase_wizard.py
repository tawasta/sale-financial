from odoo import _, fields, models


class SaleToPurchaseWizard(models.TransientModel):

    _inherit = "sale.to.purchase.wizard"

    def get_customer_code(self, product, purchase_order):

        for partner_info in product.customer_ids:
            if (
                partner_info.name.id == self.customer_id.id
                and partner_info.company_id.id == purchase_order.company_id.id
            ):
                return partner_info.product_code

        return False

    def create_purchase_line(self, current_sale_line, purchase_order):

        res = super().create_purchase_line(current_sale_line, purchase_order)

        if self.add_customer_codes:
            code = self.get_customer_code(res.product_id, purchase_order)
            if code:
                res.name += _("\nCustomer's code: {}".format(code))

        return res

    add_customer_codes = fields.Boolean(
        string="Show Customer Product Codes",
        default=True,
        help=(
            """If the sold products have customer-specific codes, add them
              to the PO line descriptions"""
        ),
    )
