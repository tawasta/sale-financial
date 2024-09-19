##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2017 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Sale Order to Purchase Order - Date Extension",
    "summary": "PO promised delivery based on vendor information",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "website": "https://gitlab.com/tawasta/odoo/sale-financial",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": [
        "base_view_inheritance_extension",
        "purchase_order_requested_receipt_date",
        "sale_order_requested_delivery_date",
        "sale_order_to_purchase_order",
    ],
    "data": [
        "wizards/sale_to_purchase_wizard.xml",
        "views/res_partner.xml",
    ],
    "demo": [],
}
