from datetime import timedelta

from odoo import api, fields, models


class SaleToPurchaseWizard(models.TransientModel):
    _inherit = "sale.to.purchase.wizard"

    def create_purchase(self, current_sale):
        res = super().create_purchase(current_sale)
        res.date_receipt_requested = self.date_request_vendor
        return res

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if self.date_request_customer:
            request_customer = self.date_request_customer
            date_request = request_customer - timedelta(days=self.vendor_dropship_delay)

            self.date_request_vendor = date_request
        else:
            self.date_request_vendor = False

    def _get_date_request_customer(self):
        sales = self._context.get("active_ids")
        sale = sales and sales[0] or False
        sale = self.env["sale.order"].browse(sale)
        if sale:
            return sale.date_delivery_requested
        else:
            return False

    vendor_dropship_delay = fields.Integer(
        related="partner_id.vendor_dropship_delay", string="Vendor delay", readonly=True
    )

    date_request_customer = fields.Datetime(
        string="Customer's Request",
        readonly=True,
        default=lambda self: self._get_date_request_customer(),
    )

    date_request_vendor = fields.Datetime(string="Date for Vendor")
