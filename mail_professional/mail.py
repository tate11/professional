from odoo import api, exceptions, fields, models
from email.utils import formataddr
import ast
import logging
_logger = logging.getLogger(__name__)

class MailTemplate(models.Model):
    _inherit = 'mail.template'

    company_id = fields.Many2one('res.company')

class MailTrackingValue(models.Model):
    _inherit = 'mail.tracking.value'

    company_id = fields.Many2one('res.company')
    
    @api.model
    def create(self, values):
        values['company_id'] = self.env['mail.message'].browse(values['mail_message_id']).company_id.id
        return super(MailTrackingValue, self).create(values)

class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def message_get_reply_to(self, res_ids, default=None):
        default = formataddr((self.env.user.name, self.env.user.email))
        return super(MailThread, self).message_get_reply_to(res_ids, default)

    def _replace_local_links(self, html, base_url=None):
        if not base_url:
            if self.env.user.company_id.website_id:
                base_url = 'http://' + str(
                    self.env.user.company_id.website_id.domain)

        return super(MailThread, self)._replace_local_links(html, base_url)

''' # TROUBLESHOOTING WHEN INCOMING MAIL DOES NOT ROUTE PROPERLY

    @api.model
    def message_process(self, model, message, custom_values=None,
                        save_original=False, strip_attachments=False,
                        thread_id=None):
                        
        _logger.debug('MailThread message_process: model = ' + str(model) + ', message = ' + str(message) + ', custom_values = ' + str(custom_values) + \
        ', save_original = ' + str(save_original) + ', strip_attachments = ' + str(strip_attachments) + ', thread_id = ' + str(thread_id) + ', context = ' + str(self.env.context))
                        
        return super(MailThread, self).message_process(model, message, custom_values,
                        save_original, strip_attachments,
                        thread_id)
                        
    @api.model
    def message_route_verify(self, message, message_dict, route, update_author=True, assert_model=True, create_fallback=True, allow_private=False):
    
        _logger.debug('MailThread message_route_verify: route = ' + str(route))
        
        return super(MailThread, self).message_route_verify(message, message_dict, route, update_author, assert_model, create_fallback, allow_private)
'''

class MailMessage(models.Model):
    _inherit = 'mail.message'
    
    company_id = fields.Many2one('res.company')

    @api.model
    def create(self, values):
        ''' New values for 'company_id', 'subject', 'email_from' '''
        #_logger.debug('MailMessage create: values = ' + str(values))
        #_logger.debug('MailMessage create: context = ' + str(self.env.context))
        #_logger.debug('MailMessage create: user.id = ' + str(self.env.user.id))

        if values.get('model'):
            try:
                values['company_id'] = self.env[values['model']].browse(values['res_id']).company_id.id
            except:
                pass
                #ParseError: "'ir.module.module' object has no attribute 'company_id'"
                #while parsing / openupgrade10 / openupgrade10 - server / addons / project / data / project_mail_template_data.xml: 121, near
                #< function
                #id = "mail_template_function_module_install_project"
                #model = "mail.template"
                #name = "send_mail"
                #eval = "[ref('mail_template_data_module_install_project'), ref('base.module_project')]" / >
        else:
            pass # get company_id from context?

        try:
            if values['model'] == 'project.task': # ParseError while parsing project/data/project_demo.xml:126
                project_name = self.env['project.task'].browse(values['res_id']).project_id.name
                task_name = self._get_record_name(values)
                values['subject'] = '[' + str(project_name) + '] ' + task_name
        except:
            pass
        
        # Send from standard email address
        email = self.env['ir.config_parameter'].get_param("mail.email_from.email")
        if not email:
            raise exceptions.UserError('no email found in system parameter mail.email_from.email')

        name = ''
        try:
            name = self.env['res.partner'].browse(values['author_id']).name
        except:
            try:
                s = values[u'email_from']
                name = s[:s.rfind("<")]
            except:
                name = ''
        values['email_from'] = formataddr((name, email))
            
        message = super(MailMessage, self).create(values)
        return message

# TEMPORARILY DEACTIVATED FOR V10
'''
class MailAlias(models.Model):
    _inherit = "mail.alias"
    
    alias_name_edit = fields.Char('Alias Name Editable')
    
    @api.model
    def create(self, vals):
        #_logger.debug('MailAlias create: vals = ' + str(vals) + ', vals.get("alias_name_edit") = ' + str(vals.get('alias_name_edit')) + ', self.env.context = ' + str(self.env.context))
        """give a unique alias name if given alias name is already assigned - and add .company_id"""
        company_id = self.env.user.company_id.id
        vals['alias_name_edit'], vals['alias_name'] = self._get_alias_names(vals.get('alias_name_edit'), company_id)
        vals['alias_defaults'] = self._get_alias_defaults(vals.get('alias_defaults'), company_id)
        return super(MailAlias, self).create(vals)
    
    @api.multi
    def write(self, vals):
        #_logger.debug('MailAlias write: vals = ' + str(vals) + '   self.ids = ' + str(self.ids) + ', self.env.context = ' + str(self.env.context))
        """give a unique alias name if given alias name is already assigned - and add .company_id"""
        self.ensure_one()
        company_id = self.env.user.company_id.id
        if ('alias_defaults' in vals) and self.ids:
            vals['alias_defaults'] = self._get_alias_defaults(vals.get('alias_defaults'), company_id)
        
        # Always use alias_name_edit to update alias_name
        vals.pop('alias_name', None)
        if ('alias_name_edit' in vals) and self.ids:
            vals['alias_name_edit'], vals['alias_name'] = self._get_alias_names(vals.get('alias_name_edit'), company_id, alias_ids=self.ids)
        return super(MailAlias, self).write(vals)
        
    @api.model
    def _get_alias_defaults(self, defaults, company_id):
        _logger.debug('MailAlias _get_alias_names_and_defaults: str(defaults) = ' + str(defaults) + ', str(type(defaults)) = ' + str(type(defaults)))
        if defaults == None:
            defaults = {}
        elif type(defaults).__name__ == 'unicode':
            defaults = ast.literal_eval(defaults)
        
        model = self._get_model(company_id)
        if model == 'res.users':
            pass
        elif model == 'project.project':
            # Task defaults
            defaults['company_id'] = company_id
            defaults['user_id'] = ''
        else:
            defaults['company_id'] = company_id
        #_logger.debug('MailAlias _get_alias_names_and_defaults: str(defaults) = ' + str(defaults))
        return str(defaults)
            
    @api.model
    def _get_alias_names(self, name, company_id, alias_ids=False):
        if not name:
            return None, None
        suffix = 'user' if self._get_model(company_id) == 'res.users' else str(company_id)
        #_logger.debug('MailAlias _get_alias_names: suffix = ' + str(suffix) + ', self.alias_parent_model_id.model = ' + str(self.alias_parent_model_id.model))
        alias_name = self._clean_and_make_unique(str(name) + '.' + suffix, alias_ids) # calls _find_unique
        alias_name_edit = alias_name.rsplit('.', 1)[0]
        return alias_name_edit, alias_name
        
    @api.model
    def _get_model(self, company_id):
        model = self.alias_parent_model_id.model
        #_logger.debug('MailAlias _get_model: self.alias_parent_model_id.model = ' + str(self.alias_parent_model_id.model))
        if not model:
            model = self.env.context.get('alias_parent_model_name')
        if not model:
            install_mode_data = self.env.context.get('install_mode_data')
            if install_mode_data:
                model = install_mode_data.get('model')
        #suffix = 'user' if model == 'res.users' else str(company_id)
        return model
        
    @api.model
    def _find_unique(self, name, alias_ids=False):
        """Find a unique alias name similar to ``name``. If ``name`` is
           already taken, make a variant by adding an integer suffix until
           an unused alias is found.
        """
        sequence = None
        while True:
            namepart = name.rsplit('.', 1)
            new_name = "%s%s.%s" % (namepart[0], sequence, namepart[1]) if sequence is not None else name
            domain = [('alias_name', '=', new_name)]
            if alias_ids:
                domain += [('id', 'not in', alias_ids)]
            if not self.search(domain):
                break
            sequence = (sequence + 1) if sequence else 2
        #_logger.debug('MailAlias _find_unique: name = ' + str(name) + ', new_name = ' + str(new_name))
        return new_name

class ResPartner(models.Model):
    _inherit = "res.partner"
        
    # The only change: base_template = self.env.ref('mail.mail_template_data_notification_email_default_professional')
    
    @api.multi
    def _notify_by_email(self, message, force_send=False, user_signature=True):
        """ Method to send email linked to notified messages. The recipients are
        the recordset on which this method is called. """
        if not self.ids:
            return True

        # existing custom notification email
        base_template = None
        if message.model:
            base_template = self.env.ref('mail.mail_template_data_notification_email_%s' % message.model.replace('.', '_'), raise_if_not_found=False)
        if not base_template:
            base_template = self.env.ref('mail.mail_template_data_notification_email_default_professional')

        base_template_ctx = self._notify_prepare_template_context(message)
        if not user_signature:
            base_template_ctx['signature'] = False
        base_mail_values = self._notify_prepare_email_values(message)

        # classify recipients: actions / no action
        if message.model and message.res_id and hasattr(self.env[message.model], '_message_notification_recipients'):
            recipients = self.env[message.model].browse(message.res_id)._message_notification_recipients(message, self)
        else:
            recipients = self.env['mail.thread']._message_notification_recipients(message, self)

        emails = self.env['mail.mail']
        recipients_nbr, recipients_max = 0, 50
        for email_type, recipient_template_values in recipients.iteritems():
            if recipient_template_values['followers']:
                # generate notification email content
                template_fol_values = dict(base_template_ctx, **recipient_template_values)  # fixme: set button_unfollow to none
                template_fol_values['button_follow'] = False
                template_fol = base_template.with_context(**template_fol_values)
                # generate templates for followers and not followers
                fol_values = template_fol.generate_email(message.id, fields=['body_html', 'subject'])
                # send email
                new_emails, new_recipients_nbr = self._notify_send(fol_values['body'], fol_values['subject'], recipient_template_values['followers'], **base_mail_values)
                emails |= new_emails
                recipients_nbr += new_recipients_nbr
            if recipient_template_values['not_followers']:
                # generate notification email content
                template_not_values = dict(base_template_ctx, **recipient_template_values)  # fixme: set button_follow to none
                template_not_values['button_unfollow'] = False
                template_not = base_template.with_context(**template_not_values)
                # generate templates for followers and not followers
                not_values = template_not.generate_email(message.id, fields=['body_html', 'subject'])
                # send email
                new_emails, new_recipients_nbr = self._notify_send(not_values['body'], not_values['subject'], recipient_template_values['not_followers'], **base_mail_values)
                emails |= new_emails
                recipients_nbr += new_recipients_nbr

        # NOTE:
        #   1. for more than 50 followers, use the queue system
        #   2. do not send emails immediately if the registry is not loaded,
        #      to prevent sending email during a simple update of the database
        #      using the command-line.
        if force_send and recipients_nbr < recipients_max and \
                (not self.pool._init or getattr(threading.currentThread(), 'testing', False)):
            emails.send()

        return True
'''
