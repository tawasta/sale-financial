import math

from odoo import _, models


class AccountMOve(models.Model):

    _inherit = "account.move"

    def _post(self, soft=True):

        product = self.env["sale.advance.payment.inv"]._default_product_id()

        for record in self:
            if record.move_type != "out_refund":
                continue

            invoice = record.reversed_entry_id

            for refund_line in invoice.invoice_line_ids:
                dp_lines = False
                if refund_line.product_id == product:
                    # Get down payment lines
                    dp_lines = refund_line.sale_line_ids.filtered(
                        lambda r: r.product_id == product
                    )

                for dp_line in dp_lines:
                    # Check which down payment lines are applicable
                    # for removal
                    sale_order = dp_line.order_id

                    if math.isclose(record.amount_untaxed, invoice.amount_untaxed):
                        # If product and untaxed amount match,
                        # remove the down payment line
                        so_msg = _(
                            "Removed down payment line for {}, "
                            "because invoice '{}' was refunded".format(
                                dp_line.price_subtotal, record.reversed_entry_id.name
                            )
                        )

                        msg = _(
                            "Removed down payment line from sale '{}'".format(
                                sale_order.name
                            )
                        )
                        # Set state to draft to avoid error about deleting
                        # line from confirmed SO
                        dp_line.state = "draft"
                        dp_line.unlink()
                    else:
                        # If refund amount doesn't match with
                        # SO line, don't delete down payment line
                        so_msg = _(
                            "Down payment '{}' was partially refunded".format(
                                record.reversed_entry_id.name
                            )
                        )
                        msg = _(
                            "Didn't remove down payment line from sale '{}'".format(
                                sale_order.name
                            )
                        )

                    record.message_post(body=msg)
                    sale_order.message_post(body=so_msg)

        return super()._post(soft)
