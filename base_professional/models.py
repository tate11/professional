import base64
import logging
import os
from decorator import decorator
from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import AccessDenied, UserError
from odoo.http import request
from odoo.tools import human_size
from odoo.addons.base.models.ir_translation import IrTranslationImport

_logger = logging.getLogger(__name__)


class MergePartnerAutomatic(models.TransientModel):
    _inherit = 'base.partner.merge.automatic.wizard'

    def _merge(self, partner_ids, dst_partner=None, extra_checks=True):
        """Company Manager can merge contacts without extra checks."""
        if self.env.user.has_group('group_company_manager'):
            extra_checks = False
        return super(MergePartnerAutomatic, self)._merge(
            partner_ids, dst_partner, extra_checks)


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    # FIX company_id for /web/content/*
    @api.model
    def create(self, values):
        name = values.get('name')
        res_model = values.get('res_model')
        if res_model == 'ir.ui.view' and name in ('/web/content/css', '/web/content/js'):
            return super(IrAttachment, self.sudo().with_context(force_company=1, default_company_id=1)).create(values)

        return super(IrAttachment, self).create(values)

    # WHEN ERROR READING FILE: LOG THE ir.attachment model & name

    # source: /base/ir/ir_attachment.py
    # - attach.datas = self._file_read(attach.store_fname, bin_size)
    # + attach.datas = self._file_read(attach.store_fname, bin_size, "model: %s, name: %s" % (attach.res_model, attach.res_name))
    @api.depends('store_fname', 'db_datas')
    def _compute_datas(self):
        bin_size = self._context.get('bin_size')
        for attach in self:
            if attach.store_fname:
                attach.datas = self._file_read(attach.store_fname, bin_size, "model: %s, name: %s" % (attach.res_model, attach.res_name))
            else:
                attach.datas = attach.db_datas

    # source: /base/ir/ir_attachment.py
    # - def _file_read(self, fname, bin_size=False):
    # + def _file_read(self, fname, bin_size=False, debug_info='no debug_info'):
    # - _logger.info("_read_file reading %s", full_path, exc_info=True)
    # + _logger.info("_file_read reading %s (%s)" % (full_path, debug_info), exc_info=True)
    @api.model
    def _file_read(self, fname, bin_size=False, debug_info='no debug_info'):
        full_path = self._full_path(fname)
        r = ''
        try:
            if bin_size:
                r = human_size(os.path.getsize(full_path))
            else:
                r = base64.b64encode(open(full_path,'rb').read())
        except (IOError, OSError):
            _logger.info("_file_read reading %s (%s)" % (full_path, debug_info), exc_info=True)
        return r

    # source: base/ir/ir_attachment.py
    # - fname = sha[:3] + '/' + sha
    # + fname = 'company/' + str(self.company_id.id) + '/' + sha[:3] + '/' + sha
    # - fname = sha[:2] + '/' + sha
    # + fname = 'company/' + str(self.company_id.id) + '/' + sha[:2] + '/' + sha
    # + _logger.debug("_GET_PATH: dirname = " + str(dirname) + ", full_path = " + str(full_path))
    # +     _logger.debug("_GET_PATH os.makedirs " + str(dirname))
    @api.model
    def _get_path(self, bin_data, sha):
        # retro compatibility
        fname = 'company/' + str(self.company_id.id) + '/' + sha[:3] + '/' + sha
        full_path = self._full_path(fname)
        if os.path.isfile(full_path):
            return fname, full_path        # keep existing path

        # scatter files across 256 dirs
        # we use '/' in the db (even on windows)
        fname = 'company/' + str(self.company_id.id) + '/' + sha[:2] + '/' + sha
        full_path = self._full_path(fname)
        dirname = os.path.dirname(full_path)
        _logger.debug("_GET_PATH: dirname = " + str(dirname) + ", full_path = " + str(full_path))
        if not os.path.isdir(dirname):
            _logger.debug("_GET_PATH os.makedirs " + str(dirname))
            os.makedirs(dirname)
        return fname, full_path


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def base_professional_create_parameters(self):
        set_param = self.sudo().set_param

        if not self.sudo().get_param('mail.email_from.email'):
            set_param('mail.email_from.email', 'admin@example.com')

        # Disable user signup and password reset until a really good testing is done
        if not self.sudo().get_param('auth_signup.reset_password'):
            set_param('auth_signup.reset_password', repr(False))
        if not self.sudo().get_param('auth_signup.allow_uninvited'):
            set_param('auth_signup.allow_uninvited', repr(False))


class IrFilters(models.Model):
    _inherit = 'ir.filters'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True,
                                 default=lambda self: self.env.user.company_id)

class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True,
                                 default=lambda self: self.env.user.company_id)


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True,
                                 default=lambda self: self.env.user.company_id)

    @api.model
    def get_view_id(self, template):
        """ Replace a view by writing the view's External ID in the KEY field. """
        view = self.search([('key','=',template),('company_id','=',self.env.user.company_id.id)], limit=1)
        if view:
            return view.id
        
        return super(IrUiView, self).get_view_id(template)

    def base_professional_deactivate_views(self):
        #self.env.ref('').write({'active': False})
        pass
