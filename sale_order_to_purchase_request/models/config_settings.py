from odoo import fields, models


class ConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    purchase_request_from_sale_buy = fields.Boolean(
        related="company_id.purchase_request_from_sale_buy", readonly=False,
    )

    purchase_request_from_sale_mrp = fields.Boolean(
        related="company_id.purchase_request_from_sale_mrp", readonly=False,
    )

    purchase_request_location_rule = fields.Selection(
        related="company_id.purchase_request_location_rule", readonly=False,
    )

    purchase_request_location_ids = fields.Many2many(
        related="company_id.purchase_request_location_ids", readonly=False,
    )
