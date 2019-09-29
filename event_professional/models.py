from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class EventMailRegistration(models.Model):
    _inherit = 'event.mail.registration'

    @api.model
    def create(self, values):
        values['company_id'] = self.env['event.registration'].browse(values['registration_id']).company_id.id
        return super(EventMailRegistration, self).create(values)