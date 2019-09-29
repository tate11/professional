# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'website_professional',

    'author': 'AppsToGROW',
    'auto_install': True,
    'category': 'Uncategorized',
    'data': [
        'templates.xml',
        'views.xml',
        'execute_functions.xml',
    ],
    'depends': ['website', 'base_professional'],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': '''
        website domain: 'default' or domain or ip address. No http(s) or port number.
    ''',
}
