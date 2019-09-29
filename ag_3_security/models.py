from odoo import fields, models

class account_account(models.Model):
    _inherit = 'account.account'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_account_tag(models.Model):
    _inherit = 'account.account.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_account_template(models.Model):
    _inherit = 'account.account.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_account_type(models.Model):
    _inherit = 'account.account.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_analytic_account(models.Model):
    _inherit = 'account.analytic.account'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_analytic_default(models.Model):
    _inherit = 'account.analytic.default'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_analytic_distribution(models.Model):
    _inherit = 'account.analytic.distribution'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_analytic_group(models.Model):
    _inherit = 'account.analytic.group'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_analytic_line(models.Model):
    _inherit = 'account.analytic.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_analytic_tag(models.Model):
    _inherit = 'account.analytic.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_asset(models.Model):
    _inherit = 'account.asset'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_asset_group(models.Model):
    _inherit = 'account.asset.group'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_asset_line(models.Model):
    _inherit = 'account.asset.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_asset_profile(models.Model):
    _inherit = 'account.asset.profile'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_asset_recompute_trigger(models.Model):
    _inherit = 'account.asset.recompute.trigger'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_bank_statement(models.Model):
    _inherit = 'account.bank.statement'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_bank_statement_cashbox(models.Model):
    _inherit = 'account.bank.statement.cashbox'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_bank_statement_line(models.Model):
    _inherit = 'account.bank.statement.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_budget_line(models.Model):
    _inherit = 'account.budget.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_budget_report(models.Model):
    _inherit = 'account.budget.report'

class account_cash_rounding(models.Model):
    _inherit = 'account.cash.rounding'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_cashbox_line(models.Model):
    _inherit = 'account.cashbox.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_chart_template(models.Model):
    _inherit = 'account.chart.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_position(models.Model):
    _inherit = 'account.fiscal.position'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_position_account(models.Model):
    _inherit = 'account.fiscal.position.account'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_position_account_template(models.Model):
    _inherit = 'account.fiscal.position.account.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_position_tax(models.Model):
    _inherit = 'account.fiscal.position.tax'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_position_tax_template(models.Model):
    _inherit = 'account.fiscal.position.tax.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_position_template(models.Model):
    _inherit = 'account.fiscal.position.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_fiscal_year(models.Model):
    _inherit = 'account.fiscal.year'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_full_reconcile(models.Model):
    _inherit = 'account.full.reconcile'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_group(models.Model):
    _inherit = 'account.group'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_incoterms(models.Model):
    _inherit = 'account.incoterms'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_invoice(models.Model):
    _inherit = 'account.invoice'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_invoice_report(models.Model):
    _inherit = 'account.invoice.report'

class account_invoice_tax(models.Model):
    _inherit = 'account.invoice.tax'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_journal(models.Model):
    _inherit = 'account.journal'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_move(models.Model):
    _inherit = 'account.move'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_move_line(models.Model):
    _inherit = 'account.move.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_partial_reconcile(models.Model):
    _inherit = 'account.partial.reconcile'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_payment(models.Model):
    _inherit = 'account.payment'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_payment_method(models.Model):
    _inherit = 'account.payment.method'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_payment_term(models.Model):
    _inherit = 'account.payment.term'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_payment_term_line(models.Model):
    _inherit = 'account.payment.term.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_reconcile_model(models.Model):
    _inherit = 'account.reconcile.model'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_reconcile_model_template(models.Model):
    _inherit = 'account.reconcile.model.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_tax(models.Model):
    _inherit = 'account.tax'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_tax_group(models.Model):
    _inherit = 'account.tax.group'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class account_tax_template(models.Model):
    _inherit = 'account.tax.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class accounting_assert_test(models.Model):
    _inherit = 'accounting.assert.test'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class barcode_nomenclature(models.Model):
    _inherit = 'barcode.nomenclature'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class barcode_rule(models.Model):
    _inherit = 'barcode.rule'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_automation(models.Model):
    _inherit = 'base.automation'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_automation_lead_test(models.Model):
    _inherit = 'base.automation.lead.test'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_automation_line_test(models.Model):
    _inherit = 'base.automation.line.test'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_mapping(models.Model):
    _inherit = 'base_import.mapping'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_char(models.Model):
    _inherit = 'base_import.tests.models.char'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_char_noreadonly(models.Model):
    _inherit = 'base_import.tests.models.char.noreadonly'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_char_readonly(models.Model):
    _inherit = 'base_import.tests.models.char.readonly'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_char_required(models.Model):
    _inherit = 'base_import.tests.models.char.required'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_char_states(models.Model):
    _inherit = 'base_import.tests.models.char.states'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_char_stillreadonly(models.Model):
    _inherit = 'base_import.tests.models.char.stillreadonly'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_complex(models.Model):
    _inherit = 'base_import.tests.models.complex'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_float(models.Model):
    _inherit = 'base_import.tests.models.float'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_m2o(models.Model):
    _inherit = 'base_import.tests.models.m2o'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_m2o_related(models.Model):
    _inherit = 'base_import.tests.models.m2o.related'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_m2o_required(models.Model):
    _inherit = 'base_import.tests.models.m2o.required'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_m2o_required_related(models.Model):
    _inherit = 'base_import.tests.models.m2o.required.related'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_o2m(models.Model):
    _inherit = 'base_import.tests.models.o2m'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_o2m_child(models.Model):
    _inherit = 'base_import.tests.models.o2m.child'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class base_import_tests_models_preview(models.Model):
    _inherit = 'base_import.tests.models.preview'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class blog_blog(models.Model):
    _inherit = 'blog.blog'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class blog_post(models.Model):
    _inherit = 'blog.post'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class blog_tag(models.Model):
    _inherit = 'blog.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class blog_tag_category(models.Model):
    _inherit = 'blog.tag.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class booking_booking(models.Model):
    _inherit = 'booking.booking'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class booking_time(models.Model):
    _inherit = 'booking.time'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class bus_bus(models.Model):
    _inherit = 'bus.bus'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class bus_presence(models.Model):
    _inherit = 'bus.presence'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class calendar_alarm(models.Model):
    _inherit = 'calendar.alarm'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class calendar_attendee(models.Model):
    _inherit = 'calendar.attendee'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class calendar_contacts(models.Model):
    _inherit = 'calendar.contacts'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class calendar_event(models.Model):
    _inherit = 'calendar.event'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class calendar_event_type(models.Model):
    _inherit = 'calendar.event.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class crm_activity_report(models.Model):
    _inherit = 'crm.activity.report'

class crm_lead(models.Model):
    _inherit = 'crm.lead'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class crm_lead_tag(models.Model):
    _inherit = 'crm.lead.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class crm_lost_reason(models.Model):
    _inherit = 'crm.lost.reason'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class crm_partner_report_assign(models.Model):
    _inherit = 'crm.partner.report.assign'

class crm_stage(models.Model):
    _inherit = 'crm.stage'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class crm_team(models.Model):
    _inherit = 'crm.team'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class crossovered_budget(models.Model):
    _inherit = 'crossovered.budget'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class date_range(models.Model):
    _inherit = 'date.range'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class date_range_type(models.Model):
    _inherit = 'date.range.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class decimal_precision(models.Model):
    _inherit = 'decimal.precision'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class decimal_precision_test(models.Model):
    _inherit = 'decimal.precision.test'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class delivery_carrier(models.Model):
    _inherit = 'delivery.carrier'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class delivery_price_rule(models.Model):
    _inherit = 'delivery.price.rule'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class digest_digest(models.Model):
    _inherit = 'digest.digest'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class digest_tip(models.Model):
    _inherit = 'digest.tip'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class donation_fundrace_partner(models.Model):
    _inherit = 'donation.fundrace.partner'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class donation_fundrace_sponsorship(models.Model):
    _inherit = 'donation.fundrace.sponsorship'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_answer(models.Model):
    _inherit = 'event.answer'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_event(models.Model):
    _inherit = 'event.event'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_event_ticket(models.Model):
    _inherit = 'event.event.ticket'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_mail(models.Model):
    _inherit = 'event.mail'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_mail_registration(models.Model):
    _inherit = 'event.mail.registration'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_question(models.Model):
    _inherit = 'event.question'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_question_report(models.Model):
    _inherit = 'event.question.report'

class event_registration(models.Model):
    _inherit = 'event.registration'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_registration_answer(models.Model):
    _inherit = 'event.registration.answer'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_sponsor(models.Model):
    _inherit = 'event.sponsor'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_sponsor_type(models.Model):
    _inherit = 'event.sponsor.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_track(models.Model):
    _inherit = 'event.track'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_track_location(models.Model):
    _inherit = 'event.track.location'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_track_stage(models.Model):
    _inherit = 'event.track.stage'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_track_tag(models.Model):
    _inherit = 'event.track.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_type(models.Model):
    _inherit = 'event.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class event_type_mail(models.Model):
    _inherit = 'event.type.mail'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fetchmail_server(models.Model):
    _inherit = 'fetchmail.server'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_service_type(models.Model):
    _inherit = 'fleet.service.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle(models.Model):
    _inherit = 'fleet.vehicle'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_assignation_log(models.Model):
    _inherit = 'fleet.vehicle.assignation.log'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_cost(models.Model):
    _inherit = 'fleet.vehicle.cost'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_log_contract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_log_fuel(models.Model):
    _inherit = 'fleet.vehicle.log.fuel'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_log_services(models.Model):
    _inherit = 'fleet.vehicle.log.services'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_model(models.Model):
    _inherit = 'fleet.vehicle.model'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_model_brand(models.Model):
    _inherit = 'fleet.vehicle.model.brand'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_odometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_state(models.Model):
    _inherit = 'fleet.vehicle.state'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_tag(models.Model):
    _inherit = 'fleet.vehicle.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class google_drive_config(models.Model):
    _inherit = 'google.drive.config'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_applicant(models.Model):
    _inherit = 'hr.applicant'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_applicant_category(models.Model):
    _inherit = 'hr.applicant.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_attendance(models.Model):
    _inherit = 'hr.attendance'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_contract(models.Model):
    _inherit = 'hr.contract'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_contract_advantage_template(models.Model):
    _inherit = 'hr.contract.advantage.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_contract_type(models.Model):
    _inherit = 'hr.contract.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_contribution_register(models.Model):
    _inherit = 'hr.contribution.register'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_department(models.Model):
    _inherit = 'hr.department'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_employee_category(models.Model):
    _inherit = 'hr.employee.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_expense(models.Model):
    _inherit = 'hr.expense'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_expense_sheet(models.Model):
    _inherit = 'hr.expense.sheet'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_job(models.Model):
    _inherit = 'hr.job'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_leave(models.Model):
    _inherit = 'hr.leave'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_leave_allocation(models.Model):
    _inherit = 'hr.leave.allocation'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_leave_report(models.Model):
    _inherit = 'hr.leave.report'

class hr_leave_type(models.Model):
    _inherit = 'hr.leave.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_payroll_structure(models.Model):
    _inherit = 'hr.payroll.structure'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_payslip(models.Model):
    _inherit = 'hr.payslip'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_payslip_input(models.Model):
    _inherit = 'hr.payslip.input'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_payslip_line(models.Model):
    _inherit = 'hr.payslip.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_payslip_run(models.Model):
    _inherit = 'hr.payslip.run'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_payslip_worked_days(models.Model):
    _inherit = 'hr.payslip.worked_days'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_recruitment_degree(models.Model):
    _inherit = 'hr.recruitment.degree'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_recruitment_source(models.Model):
    _inherit = 'hr.recruitment.source'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_recruitment_stage(models.Model):
    _inherit = 'hr.recruitment.stage'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_rule_input(models.Model):
    _inherit = 'hr.rule.input'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_rule_qty_rate_amount(models.Model):
    _inherit = 'hr.rule.qty_rate_amount'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_salary_rule(models.Model):
    _inherit = 'hr.salary.rule'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_salary_rule_category(models.Model):
    _inherit = 'hr.salary.rule.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class hr_timesheet_attendance_report(models.Model):
    _inherit = 'hr.timesheet.attendance.report'

class iap_account(models.Model):
    _inherit = 'iap.account'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class im_livechat_channel(models.Model):
    _inherit = 'im_livechat.channel'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class im_livechat_channel_rule(models.Model):
    _inherit = 'im_livechat.channel.rule'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class im_livechat_report_channel(models.Model):
    _inherit = 'im_livechat.report.channel'

class im_livechat_report_operator(models.Model):
    _inherit = 'im_livechat.report.operator'

class ir_act_report_xml(models.Model):
    _inherit = 'ir.actions.report'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_attachment(models.Model):
    _inherit = 'ir.attachment'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_default(models.Model):
    _inherit = 'ir.default'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_exports(models.Model):
    _inherit = 'ir.exports'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_exports_line(models.Model):
    _inherit = 'ir.exports.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_filters(models.Model):
    _inherit = 'ir.filters'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_mail_server(models.Model):
    _inherit = 'ir.mail_server'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_model_data(models.Model):
    _inherit = 'ir.model.data'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_property(models.Model):
    _inherit = 'ir.property'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_sequence(models.Model):
    _inherit = 'ir.sequence'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_sequence_date_range(models.Model):
    _inherit = 'ir.sequence.date_range'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_translation(models.Model):
    _inherit = 'ir.translation'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_ui_view(models.Model):
    _inherit = 'ir.ui.view'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class ir_ui_view_custom(models.Model):
    _inherit = 'ir.ui.view.custom'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class l10n_no_hr_payroll_amelding(models.Model):
    _inherit = 'l10n_no_hr_payroll.amelding'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class l10n_no_hr_payroll_tabelltrekk(models.Model):
    _inherit = 'l10n_no_hr_payroll.tabelltrekk'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class link_tracker(models.Model):
    _inherit = 'link.tracker'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class link_tracker_click(models.Model):
    _inherit = 'link.tracker.click'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class link_tracker_code(models.Model):
    _inherit = 'link.tracker.code'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_activity(models.Model):
    _inherit = 'mail.activity'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_activity_type(models.Model):
    _inherit = 'mail.activity.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_alias(models.Model):
    _inherit = 'mail.alias'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_blacklist(models.Model):
    _inherit = 'mail.blacklist'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_channel(models.Model):
    _inherit = 'mail.channel'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_channel_partner(models.Model):
    _inherit = 'mail.channel.partner'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_followers(models.Model):
    _inherit = 'mail.followers'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mail(models.Model):
    _inherit = 'mail.mail'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mail_statistics(models.Model):
    _inherit = 'mail.mail.statistics'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing(models.Model):
    _inherit = 'mail.mass_mailing'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing_campaign(models.Model):
    _inherit = 'mail.mass_mailing.campaign'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing_contact(models.Model):
    _inherit = 'mail.mass_mailing.contact'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing_list(models.Model):
    _inherit = 'mail.mass_mailing.list'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing_contact_list_rel(models.Model):
    _inherit = 'mail.mass_mailing.list_contact_rel'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing_stage(models.Model):
    _inherit = 'mail.mass_mailing.stage'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_mass_mailing_tag(models.Model):
    _inherit = 'mail.mass_mailing.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_message(models.Model):
    _inherit = 'mail.message'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_message_subtype(models.Model):
    _inherit = 'mail.message.subtype'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_moderation(models.Model):
    _inherit = 'mail.moderation'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_message_res_partner_needaction_rel(models.Model):
    _inherit = 'mail.notification'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_shortcode(models.Model):
    _inherit = 'mail.shortcode'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_statistics_report(models.Model):
    _inherit = 'mail.statistics.report'

class mail_template(models.Model):
    _inherit = 'mail.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mail_tracking_value(models.Model):
    _inherit = 'mail.tracking.value'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_bom(models.Model):
    _inherit = 'mrp.bom'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_bom_line(models.Model):
    _inherit = 'mrp.bom.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_document(models.Model):
    _inherit = 'mrp.document'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_production(models.Model):
    _inherit = 'mrp.production'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_routing(models.Model):
    _inherit = 'mrp.routing'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_routing_workcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_unbuild(models.Model):
    _inherit = 'mrp.unbuild'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_workcenter(models.Model):
    _inherit = 'mrp.workcenter'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_workcenter_productivity(models.Model):
    _inherit = 'mrp.workcenter.productivity'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_workcenter_productivity_loss(models.Model):
    _inherit = 'mrp.workcenter.productivity.loss'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_workcenter_productivity_loss_type(models.Model):
    _inherit = 'mrp.workcenter.productivity.loss.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class mrp_workorder(models.Model):
    _inherit = 'mrp.workorder'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class payment_acquirer(models.Model):
    _inherit = 'payment.acquirer'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class payment_icon(models.Model):
    _inherit = 'payment.icon'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class payment_token(models.Model):
    _inherit = 'payment.token'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class payment_transaction(models.Model):
    _inherit = 'payment.transaction'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class pos_category(models.Model):
    _inherit = 'pos.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class pos_config(models.Model):
    _inherit = 'pos.config'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class pos_order(models.Model):
    _inherit = 'pos.order'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class pos_order_line(models.Model):
    _inherit = 'pos.order.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class pos_pack_operation_lot(models.Model):
    _inherit = 'pos.pack.operation.lot'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class pos_session(models.Model):
    _inherit = 'pos.session'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class procurement_group(models.Model):
    _inherit = 'procurement.group'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_attribute(models.Model):
    _inherit = 'product.attribute'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_attribute_custom_value(models.Model):
    _inherit = 'product.attribute.custom.value'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_attribute_value(models.Model):
    _inherit = 'product.attribute.value'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_category(models.Model):
    _inherit = 'product.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_image(models.Model):
    _inherit = 'product.image'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_packaging(models.Model):
    _inherit = 'product.packaging'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_price_history(models.Model):
    _inherit = 'product.price.history'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_pricelist(models.Model):
    _inherit = 'product.pricelist'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_pricelist_item(models.Model):
    _inherit = 'product.pricelist.item'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_product(models.Model):
    _inherit = 'product.product'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_public_category(models.Model):
    _inherit = 'product.public.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_putaway(models.Model):
    _inherit = 'product.putaway'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_removal(models.Model):
    _inherit = 'product.removal'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_style(models.Model):
    _inherit = 'product.style'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_supplierinfo(models.Model):
    _inherit = 'product.supplierinfo'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_template(models.Model):
    _inherit = 'product.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_template_attribute_exclusion(models.Model):
    _inherit = 'product.template.attribute.exclusion'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_template_attribute_line(models.Model):
    _inherit = 'product.template.attribute.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class product_template_attribute_value(models.Model):
    _inherit = 'product.template.attribute.value'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class project_profitability_report(models.Model):
    _inherit = 'project.profitability.report'

class project_project(models.Model):
    _inherit = 'project.project'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class project_sale_line_employee_map(models.Model):
    _inherit = 'project.sale.line.employee.map'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class project_tags(models.Model):
    _inherit = 'project.tags'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class project_task(models.Model):
    _inherit = 'project.task'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class project_task_type(models.Model):
    _inherit = 'project.task.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class purchase_bill_union(models.Model):
    _inherit = 'purchase.bill.union'

class purchase_order(models.Model):
    _inherit = 'purchase.order'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class purchase_report(models.Model):
    _inherit = 'purchase.report'

class purchase_requisition(models.Model):
    _inherit = 'purchase.requisition'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class purchase_requisition_line(models.Model):
    _inherit = 'purchase.requisition.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class purchase_requisition_type(models.Model):
    _inherit = 'purchase.requisition.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class rating_rating(models.Model):
    _inherit = 'rating.rating'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class report_all_channels_sales(models.Model):
    _inherit = 'report.all.channels.sales'

class report_layout(models.Model):
    _inherit = 'report.layout'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class report_paperformat(models.Model):
    _inherit = 'report.paperformat'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class report_pos_order(models.Model):
    _inherit = 'report.pos.order'

class report_project_task_user(models.Model):
    _inherit = 'report.project.task.user'

class report_stock_forecast(models.Model):
    _inherit = 'report.stock.forecast'

class res_company(models.Model):
    _inherit = 'res.company'

class res_country_group(models.Model):
    _inherit = 'res.country.group'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_currency_rate(models.Model):
    _inherit = 'res.currency.rate'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_field(models.Model):
    _inherit = 'res.field'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_field_selection_value(models.Model):
    _inherit = 'res.field.selection_value'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_field_value(models.Model):
    _inherit = 'res.field.value'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner(models.Model):
    _inherit = 'res.partner'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_activation(models.Model):
    _inherit = 'res.partner.activation'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_autocomplete_sync(models.Model):
    _inherit = 'res.partner.autocomplete.sync'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_bank(models.Model):
    _inherit = 'res.partner.bank'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_category(models.Model):
    _inherit = 'res.partner.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_grade(models.Model):
    _inherit = 'res.partner.grade'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_tag(models.Model):
    _inherit = 'res.partner.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_partner_title(models.Model):
    _inherit = 'res.partner.title'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class res_users(models.Model):
    _inherit = 'res.users'

class res_users_log(models.Model):
    _inherit = 'res.users.log'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class resource_calendar(models.Model):
    _inherit = 'resource.calendar'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class resource_calendar_attendance(models.Model):
    _inherit = 'resource.calendar.attendance'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class resource_calendar_leaves(models.Model):
    _inherit = 'resource.calendar.leaves'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class resource_resource(models.Model):
    _inherit = 'resource.resource'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class resource_test(models.Model):
    _inherit = 'resource.test'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_order(models.Model):
    _inherit = 'sale.order'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_order_option(models.Model):
    _inherit = 'sale.order.option'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_order_template(models.Model):
    _inherit = 'sale.order.template'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_order_template_line(models.Model):
    _inherit = 'sale.order.template.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_order_template_option(models.Model):
    _inherit = 'sale.order.template.option'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class sale_report(models.Model):
    _inherit = 'sale.report'

class slide_category(models.Model):
    _inherit = 'slide.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class slide_channel(models.Model):
    _inherit = 'slide.channel'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class slide_embed(models.Model):
    _inherit = 'slide.embed'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class slide_slide(models.Model):
    _inherit = 'slide.slide'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class slide_tag(models.Model):
    _inherit = 'slide.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class snailmail_letter(models.Model):
    _inherit = 'snailmail.letter'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_fixed_putaway_strat(models.Model):
    _inherit = 'stock.fixed.putaway.strat'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_inventory(models.Model):
    _inherit = 'stock.inventory'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_inventory_line(models.Model):
    _inherit = 'stock.inventory.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_location(models.Model):
    _inherit = 'stock.location'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_location_route(models.Model):
    _inherit = 'stock.location.route'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_move(models.Model):
    _inherit = 'stock.move'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_move_line(models.Model):
    _inherit = 'stock.move.line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_package_level(models.Model):
    _inherit = 'stock.package_level'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_picking(models.Model):
    _inherit = 'stock.picking'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_picking_type(models.Model):
    _inherit = 'stock.picking.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_production_lot(models.Model):
    _inherit = 'stock.production.lot'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_quant(models.Model):
    _inherit = 'stock.quant'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_quant_package(models.Model):
    _inherit = 'stock.quant.package'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_rule(models.Model):
    _inherit = 'stock.rule'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_scrap(models.Model):
    _inherit = 'stock.scrap'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_warehouse(models.Model):
    _inherit = 'stock.warehouse'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class stock_warehouse_orderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_label(models.Model):
    _inherit = 'survey.label'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_page(models.Model):
    _inherit = 'survey.page'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_question(models.Model):
    _inherit = 'survey.question'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_stage(models.Model):
    _inherit = 'survey.stage'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_survey(models.Model):
    _inherit = 'survey.survey'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_user_input(models.Model):
    _inherit = 'survey.user_input'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class survey_user_input_line(models.Model):
    _inherit = 'survey.user_input_line'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class theme_ir_attachment(models.Model):
    _inherit = 'theme.ir.attachment'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class theme_ir_ui_view(models.Model):
    _inherit = 'theme.ir.ui.view'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class theme_website_menu(models.Model):
    _inherit = 'theme.website.menu'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class theme_website_page(models.Model):
    _inherit = 'theme.website.page'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class uom_category(models.Model):
    _inherit = 'uom.category'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class uom_uom(models.Model):
    _inherit = 'uom.uom'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class utm_campaign(models.Model):
    _inherit = 'utm.campaign'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class utm_medium(models.Model):
    _inherit = 'utm.medium'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class utm_source(models.Model):
    _inherit = 'utm.source'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class web_editor_converter_test(models.Model):
    _inherit = 'web_editor.converter.test'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class web_editor_converter_test_sub(models.Model):
    _inherit = 'web_editor.converter.test.sub'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class website(models.Model):
    _inherit = 'website'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class website_event_menu(models.Model):
    _inherit = 'website.event.menu'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class website_menu(models.Model):
    _inherit = 'website.menu'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class website_page(models.Model):
    _inherit = 'website.page'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class website_redirect(models.Model):
    _inherit = 'website.redirect'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
