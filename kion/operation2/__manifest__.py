# -*- coding: utf-8 -*-

{
    'name': 'Operation2',
    'version': '1.0.0',
    'sequence': '-2',
    'category': 'Hospital',
    'author': 'Mohamed Mamdouh',
    'summary': 'Odoo Mates Hospital Management Sysytem',
    'description': """Odoo 15
    Odoo Mates
    Hospital Management Sysytem
    """,
    'depends': ['mail', 'product'],
    'data': [
        'security\ir.model.access.csv',
        'views\menu.xml',
        'views/accident_insurance.xml',
        'views\prospect.xml',
        'views\client.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
