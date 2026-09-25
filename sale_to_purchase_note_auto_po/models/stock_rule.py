from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _prepare_purchase_order(self, company_id, origins, values):
        vals = super()._prepare_purchase_order(company_id, origins, values)

        # Any automatically generated PO whose procurement group traces back
        # to a sale order (regular MTO/Buy replenishment or subcontracting -
        # both go through this same group_id.sale_id link) gets the note.
        first_value = values[0]
        group = first_value.get("group_id")
        sale_order = group and group.sale_id

        if not sale_order:
            return vals

        vals["sale_order_id"] = sale_order.id

        if sale_order.client_order_ref:
            supplier = first_value.get("supplier")
            partner = supplier.partner_id if supplier else False
            vals["notes"] = "{} {}".format(
                sale_order.company_id.with_context(
                    lang=partner and partner.lang
                ).sale_to_purchase_note_text,
                sale_order.client_order_ref,
            )

        return vals
