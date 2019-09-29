from odoo import api, fields, models, tools
import logging

_logger = logging.getLogger(__name__)


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    # TODO: The method doesn't work with execute_functions (and it is anyway good to manually create the default website)
    @api.multi
    def website_professional_create_default_website(self):

        # Create default website
        # website.py: When website does not exist, return 'default' website
        default_website = self.env['website'].search([('domain', '=', 'default')], limit=1)
        if not default_website:
            self.env['website'].create(
                {'name': 'DEFAULT WEBSITE', 'company_id': 1, 'user_id': self.env.ref('base.public_user').id,
                 'domain': 'default'})


class Website(models.Model):
    _inherit = 'website'

    _sql_constraints = [('domain_uniq', 'unique(domain)', 'Website Domain must be unique!')]

    # When website does not exist, return 'default' website
    # TODO: improve
    @tools.cache('domain_name')
    def _get_current_website_id(self, domain_name, country_id, fallback):
        """ Reminder : cached method should be return record, since they will use a closed cursor. """
        website = self.search([('domain', '=', domain_name)], limit=1)
        if not website:
            website = self.search([('domain', '=', 'default')], limit=1)
        return website.id
