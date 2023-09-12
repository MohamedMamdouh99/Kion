from odoo import models, fields, api


class AddEmployeeFields(models.Model):
    _inherit = 'hr.employee'
    cost_center=fields.Char(string='Cost Center')
    filecode = fields.Float(string='annual increase',compute='valuesof_rate')
    bloodgroup = fields.Selection(
        [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'),
         ('AB-', 'AB-')], string='Blood Group')
    religion = fields.Selection([('Muslim', 'Muslim'), ('Christianity', 'Christianity')], string='Religion')
    upload_id = fields.Binary(string='upload id', help="Select image here")
    id_expiry_date = fields.Date(string='Id expiry date')
    id_issue_date = fields.Date(string='Id issue date')
    passport_expiry_date = fields.Date(string='passport_expiry_date')
    upload_passport = fields.Binary(string='upload passport', help="Select image here")
    military_status = fields.Selection([('Exemption', 'Exemption'), (' had finished', ' had finished')],
                                       string='military status')
    military_date = fields.Date(string='military date')
    military_certification_class = fields.Selection(
        [('bad', 'bad'), (' good', ' good'), ('a good idol', 'a good idol')], string='military certification class')
    military_certification_code = fields.Char(string='military certification code')
    upload_military_certification = fields.Binary(string='upload military certification', help="Select image here")
    total_experience_in_years = fields.Integer(string='total experience in years')
    upload_bachelor_certification = fields.Binary(string='upload bachelor certification', help="Select image here")
    upload_criminal_newspaper = fields.Binary(string='upload criminal newspaper', help="Select image here")
    upload_work_permit = fields.Binary(string='upload work permit', help="Select image here")
    upload_social_insurance_print = fields.Binary(string='upload social insurance print', help="Select image here")
    employee_rate = fields.Char(string='Employee RATE',compute='get_value')

    def get_value(self):
        value=self.env['employee.evaluation'].search([('employee_id.id','=',self.id)]).employee_rate
        self.employee_rate=value

    def valuesof_rate(self):
        value = self.env['add.emlpoyee.rate'].search([])

        if self.employee_rate == 'A':
            self.filecode = value.value_a
        elif self.employee_rate == 'B':
            self.filecode = value.value_b
        elif self.employee_rate == 'c':
            self.filecode = value.value_c
        elif self.employee_rate == 'c-':
            self.filecode = value.value_c_minus
        else:
            self.filecode = 0
