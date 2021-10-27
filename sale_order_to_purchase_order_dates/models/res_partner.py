from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    vendor_dropship_delay = fields.Integer(
        string="Delivery delay to end customer",
        help="Used for compensation calculation when determining the "
        "requested delivery date for a purchase order",
    )
