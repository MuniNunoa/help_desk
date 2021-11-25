# -*- coding: utf-8 -*-
{
    'name': "Tickets",

    'summary': """
        Mesa de ayuda, soporte y solicitudes a través de tickets""",

    'description': """
        Long description of module's purpose
    """,

    'author': "José Miguel Cordero, Municipalidad de Ñuñoa",
    'website': "https://github.com/josemcorderoc/odoo-nunoa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'ab_openstreetmap'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/tickets.street.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}