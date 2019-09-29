from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)

import odoo.sql_db


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.multi
    def stock_professional_deactivate_blocking_ir_rules(self):
        for ext_id in ['stock.stock_location_comp_rule']:
            try:
                sql = "UPDATE ir_rule SET active = false WHERE id = " + str(self.env.ref(ext_id).id) + ";"
                self.env.cr.execute(sql)
            except:
                pass

    @api.multi
    def stock_professional_deactivate_locations(self):
        # Hide system stock locations that is auto-created per company
        for location_name in ['WH', 'Stock', 'My Company: Transit Location']:
            locations = self.env['stock.location'].search([('active','=',True),('company_id','=',1),('name','=',location_name)])
            for location in locations:
                location.active = False
