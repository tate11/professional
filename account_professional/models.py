from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AccountAccountType(models.Model):
    _inherit = 'account.account.type'

    company_id = fields.Many2one('res.company', "Company", default=lambda self: self.env.user.company_id)


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    #company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id) # KeyError: 'currency_id'


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class AccountInvoiceTax(models.Model):
    _inherit = "account.invoice.tax"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.multi
    def import_statement(self):
        """Overriding the default import_statement method.
        For now, go to Bank Statements, where users can click the "Import" button (base_import feature).

        Going directly to "Import" button requires passing the 'journal_id' in context.
        Client action puts the context in the URL, not in real context.

        TODO: Use the default import_statement method, process multiple formats of bank statements."""

        return self.open_action()


class AccountMove(models.Model):
    _inherit = "account.move"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class AccountPartialReconcile(models.Model):
    _inherit = "account.partial.reconcile"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class AccountPayment(models.Model):
    _inherit = "account.payment"

    company_id = fields.Many2one(related='', default=lambda self: self.env.user.company_id)


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.multi
    def remove_tax_groups_from_base_groups(self):
        # Define "Tax display B2B/B2C" on each user, not in base groups.
        subtotal_id = self.env.ref('account.group_show_line_subtotals_tax_excluded').id
        total_id = self.env.ref('account.group_show_line_subtotals_tax_included').id
        for group_to_update in ['base.group_user', 'base.group_portal', 'base.group_public']:
            self.env.ref(group_to_update).write({'implied_ids': [(3, subtotal_id), (3, total_id)]})


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Chart of accounts can be installed only when there are no accounts.
    # Receivable and payable accounts are mandatory fields on partners.
    # So if a company wants to install a chart of accounts, this must be done BEFORE registering any partner.
    # This is not acceptable, so receivable and payable accounts should not be mandatory fields on partners.

    property_account_payable_id = fields.Many2one(required=False)
    property_account_receivable_id = fields.Many2one(required=False)