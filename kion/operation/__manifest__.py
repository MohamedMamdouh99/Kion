# -*- coding: utf-8 -*-
{
    'name': "operation",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','contacts','base','prt_mail_messages'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_cron_data.xml',
        'data/sea_and_air_report.xml',
        'data/calims_after_fix.xml',
        'data/land_transprt_report.xml',
        'data/cash_transfer_insurance_report.xml',
        'data/calims_before_fix.xml',
        'data/accident_insurance.xml',
        'data/equal_request_report.xml',
        'data/car_enter_report.xml',
        'data/client_document_report.xml',
        'data/exit_permission_report.xml',
        'wizard/wizardview.xml',
        'views/views.xml',
        'views/claims.xml',
        'views/car_enter_claims.xml',
        'views/choose_model.xml',
        'views/exit_permison_claims.xml',
        'views/claims_after_fix.xml',
        'views/equal_claims_form.xml',
        'views/client_documnet_client.xml',
        'views/email_template_claims.xml',
        'views/land_transfer.xml',
        'views/accident_insurance.xml',
        'views/policy.xml',
        'views/Cash_transfer_insurance.xml',
        'views/sea_and_air.xml',
        'views/templates.xml',
        'views/email_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
