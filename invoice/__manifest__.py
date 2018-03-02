# -*- coding: utf-8 -*-
{
    'name': "Invoice Royalties",

    'summary': """""",

    'description': """
        Genera un calculo de de regalias cuando el precio del producto es 0.00 y suma el costo total de las regalias en Lps.
    """,

    'author': "Calix.Inc",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inovice',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/account_invoice_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}