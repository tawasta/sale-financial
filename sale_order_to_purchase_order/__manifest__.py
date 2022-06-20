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
    "name": "Sale Order to Purchase Order",
    "summary": "Button for creating a PO from SO, containing the same lines",
    "version": "14.0.1.2.3",
    "category": "Sales",
    "website": "https://gitlab.com/tawasta/odoo/sale-financial",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["sale_stock", "purchase", "onchange_helper"],
    "data": [
        "security/model_access.xml",
        "wizards/sale_to_purchase_wizard.xml",
        "views/purchase_order.xml",
        "views/res_company.xml",
        "views/sale_order.xml",
    ],
    "demo": [],
}
