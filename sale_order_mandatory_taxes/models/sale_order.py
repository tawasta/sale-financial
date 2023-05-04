from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):

    _inherit = "sale.order"

    bypass_mandatory_tax = fields.Boolean(
        string="Allow confirming without taxes",
        default=False,
        copy=False,
    )

    def action_confirm(self):
        for record in self:
            lines_without_taxes = record.order_line.filtered(
                lambda l: not l.tax_id and not l.display_type
            )

            if lines_without_taxes and not record.bypass_mandatory_tax:
                raise ValidationError(_("Please set taxes for all the lines."))

        return super().action_confirm()
