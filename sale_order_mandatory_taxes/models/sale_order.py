from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):

    _inherit = "sale.order"

    order_line_without_tax_ids = fields.One2many(
        comodel_name="sale.order.line",
        inverse_name="order_id",
        domain=[("tax_id", "=", False)],
    )
    bypass_mandatory_tax = fields.Boolean(
        string="Allow confirming without taxes",
        default=False,
        copy=False,
    )

    def action_confirm(self):
        for record in self:
            if record.order_line_without_tax_ids and not record.bypass_mandatory_tax:
                raise ValidationError(_("Please set taxes for all the lines."))

        return super().action_confirm()
