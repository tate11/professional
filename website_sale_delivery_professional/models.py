from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # 'force_company'
    # source: website_sale_delivery/models/sale_order.py
    def _get_delivery_methods(self):
        address = self.partner_shipping_id
        company_id = self.env.context.get('force_company',
                                          self.env.user.company_id.id)
        return self.env['delivery.carrier'].sudo().search(
            [('website_published', '=', True), ('company_id', '=', company_id)]
        ).available_carriers(address)