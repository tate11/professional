# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'mail_professional',

    'author': 'AppsToGROW',
    'auto_install': True,
    'category': 'Uncategorized',
    'data': [
        'ir.model.access.csv',
        'ir.rule.csv',
        'views.xml',
    ],
    'depends': [
        'mail',
        'mail_new_fields',
        'base_professional',
        'website_new_fields'
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',
}
