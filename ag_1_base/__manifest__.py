# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'AG 1 Base',
    'summary': 'Install this first',

    'author': 'Henrik Norlin',
    'author': 'AppsToGROW',
    'category': 'Uncategorized',
    'depends': [
        'point_of_sale', # (depends on stock_account) otherwise ParseError: "null value in column "categ_id" violates not-null constraint
        'delivery', # (depends on sale_stock) otherwise ParseError: "null value in column "categ_id" violates not-null constraint
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',
}
