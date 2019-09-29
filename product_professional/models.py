from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.multi
    def deactivate_system_pricelists(self):
        # /shop does not work for clients when company 1 has any active pricelist (and product?).
        pricelists = self.env['product.pricelist'].search([('active', '=', True), ('company_id', '=', 1)])
        for pricelist in pricelists:
            pricelist.write({'active': False})


class ProductCategory(models.Model):
    _inherit = 'product.category'

    company_id = fields.Many2one('res.company')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # source: product/models/product_template.py
    # The original categ_id default=_get_default_category_id looks up ref('product.product_category_all') and causes access error.
    # 12.0: raise_if_not_found=False
    #def _get_default_category_id(self):
    #    if self._context.get('categ_id') or self._context.get('default_categ_id'):
    #        return self._context.get('categ_id') or self._context.get('default_categ_id')
    #    category = self.env['product.category'].search([('company_id', '=', self.env.user.company_id.id)], order='id',
    #                                                   limit=1)
    #    return category and category.id or False

    #categ_id = fields.Many2one(default=_get_default_category_id)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    #property_product_pricelist = fields.Many2one(compute='_compute_product_pricelist')

    # The function is always executed as SUPERUSER. Get the correct company_id from the partner.
    # source: product/models/res_partner.py
    # - p.property_product_pricelist = self.env['product.pricelist']._get_partner_pricelist(p.id)
    # + p.property_product_pricelist = self.env['product.pricelist']._get_partner_pricelist(p.id, p.company_id.id)
    # seems to be fixed in https://github.com/odoo/odoo/blob/12.0/addons/product/models/res_partner.py
    #@api.multi
    #@api.depends('country_id')
    #def _compute_product_pricelist(self):
    #    for p in self:
    #        if not isinstance(p.id, models.NewId):  # if not onchange
    #            company_id = self.env.context.get('force_company', self.env.user.company_id.id)
    #            uid = self.env.context.get('uid', self.env.user.id)
    #            p.property_product_pricelist = self.env['product.pricelist']._get_partner_pricelist(p.id, p.company_id.id)
