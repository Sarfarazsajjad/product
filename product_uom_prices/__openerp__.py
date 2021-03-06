# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Product UOM Prices',
    'version': '8.0.0.8.0',
    'category': 'base.module_category_knowledge_management',
    'description': """
Product UOM Prices
==================
* Add a o2m field on products to allow defining prices in different uoms
* Add a new type of price calculation on pricelists (for the new o2m field
    on products)
* Change domain on sale order lines so that only defined uoms can be choosen.

Video TUTORIAL: https://www.youtube.com/watch?v=-jGsbEZDOJE
""",
    'author': 'ADHOC SA.',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'product_sale_uom',
        'product_computed_list_price',
        ],
    'test': [],
    'demo': [
        'demo/product_demo.xml',
    ],
    'data': [
        'view/product_view.xml',
    ],
    'installable': True
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
