# -*- coding: utf-8 -*-
{
    'name': "RRHH",

    'summary': """
  """,

    'description': """
       Agrega datos personales a la ficha de Empleado
    """,

    'author': "Calix.Inc",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Employee',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}