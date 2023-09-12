from odoo import models, fields, api

class EmployeeAppriasal(models.Model):
    _name='employee.evaluation'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    employee_id=fields.Many2one('hr.employee',string='emlpoyee',tracking=True)

    employee_rate=fields.Selection([('A','A'),('B','B'),('c','c'),('c-','c-')],string='Employee RATE',tracking=True)




    _sql_constraints = [
        ('field_unique',
         'unique(employee_id)',
         'Choose another employee - you choose hime before!')
    ]

















class AddRAtting(models.Model):
    _name='add.emlpoyee.rate'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    value_a = fields.Float(string='value of class A',tracking=True)
    value_b = fields.Float(string='value of class B',tracking=True)
    value_c = fields.Float(string='value of class C',tracking=True)
    value_c_minus = fields.Float(string='value of class C-',tracking=True)


    #
    # A
    # 10 %
    # B
    # 8 %
    # C
    # 5 %
    # C - 0 %
    # def enter_values(self):
    #     value = self.env['hr.employee'].search([('id','=',self.employee_id.id)])
    #     rate=value.employee_rate
    #
    #     if rate == 'A':
    #         if self.value_a:
    #             value.filecode=self.value_a
    #         else:
    #             value.filecode=0
    #     elif rate == 'B':
    #         if self.value_b:
    #             value.filecode=self.value_b
    #         else:
    #             value.filecode=0
    #     elif rate == 'c':
    #         if self.value_c:
    #             value.filecode = self.value_c
    #         else:
    #             value.filecode = 0
    #
    #     elif rate == 'c-':
    #         value.filecode = 0
    #     else:
    #         value.filecode = 0



