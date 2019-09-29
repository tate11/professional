from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # 'force_company'
    # source: sale_stock/models/sale_order.py
    # - company = self.env.user.company_id.id
    # + company = self.env.context.get('force_company', self.env.user.company_id.id)
    @api.model
    def _default_warehouse_id(self):
        company = self.env.context.get('force_company', self.env.user.company_id.id)
        warehouse_ids = self.env['stock.warehouse'].search([('company_id', '=', company)], limit=1)
        return warehouse_ids

    warehouse_id = fields.Many2one(default=_default_warehouse_id)