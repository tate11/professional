import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'
    
    @api.model
    def create(self, values):
        if 'slip_id' in values and self.env['hr.payslip'].browse(values['slip_id']).state == 'done':
            raise UserError("Cannot create the Payslip Line, because the Payslip is done!")
        return super(HrPayslipLine, self).create(values)
    
    @api.multi
    def write(self, values):
        for line in self:
            if line.slip_id.state == 'done':
                raise UserError("Cannot edit the Payslip Line(s), because the Payslip is done!")
            if 'slip_id' in values and self.env['hr.payslip'].browse(values['slip_id']).state == 'done':
                raise UserError("Cannot edit the Payslip Line(s), because the Payslip is done!")
        return super(HrPayslipLine, self).write(values)
    
    @api.multi
    def unlink(self):
        for line in self:
            if line.slip_id.state == 'done':
                raise UserError("Cannot delete the Payslip Line(s), because the Payslip is done!")
        return super(HrPayslipLine, self).unlink()
    

class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    @api.multi
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('code'):
            default['code'] = _("%s (copy)") % self.code
        if not default.get('name'):
            default['name'] = _("%s (copy)") % self.name
        return super(HrSalaryRule, self).copy(default)

    _sql_constraints = [
        ('company_code_uniq', 'unique (company_id, code)', "The rule's code must be unique!"),
    ]
    


