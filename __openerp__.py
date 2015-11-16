# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Oy Tawasta Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale-Opportunity Integration',
    'category': 'Sale',
    'version': '8.0.0.3.1',
    'author': 'Oy Tawasta Technologies Ltd.',
    'website': 'http://www.tawasta.fi',
    'depends': [
        'crm',
        'crm_lead_to_sale',
        'crm_simplification',
        'sale',
        'sale_crm',
    ],
    'description': '''
Sale-Opportunity Integration
==================

Links opportunity and sale order to work together as seamlessly as possible

Features
========
* Adds sale actions to crm case stage
* Auto-creates SO when the opportunity reaches to certain state
* Auto-cancels SO if the opportunity is canceled
* Adds sale orders lines to the opportunity
* Syncs opportunity and sale order descriptions
''',
    'data': [
        'views/crm_lead_form.xml',

        'views/crm_case_stage_form.xml',
        'views/crm_case_stage_tree.xml',

        'data/crm_case_stage_data.xml',
    ],
}
