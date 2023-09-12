from odoo import fields, models, api


class Prospect(models.Model):
    _name = 'prospect'
    _description = 'Description'
    _rec_name = 'client'

    client = fields.Many2one(
        comodel_name='client',
        string='Client',
        required=True)

    phone_number = fields.Char(string='Phone Number', readonly=True)
    address = fields.Text(string='Address', readonly=True)
    email = fields.Text(string='E-mail', readonly=True)

    contact_person_name = fields.Char(string='Contact Person Name', readonly=True)
    designation = fields.Char(string='Designation', readonly=True)
    contact_person_phone = fields.Char(string='Phone', readonly=True)
    contact_person_email = fields.Char(string='Email', readonly=True)
    attachments = fields.Many2many(
        comodel_name='ir.attachment',
        relation='prospect_attachment_rel',
        column1='prospect_id',
        column2='attachment_id',
        string='Attachments',
    )

    business_owner = fields.Char(string='Business Owner', required='True')
    type_of_business = fields.Selection([
        ('new', 'New'),
        ('rollover', 'Rollover'),
        ('renew', 'Renew')
    ], string='Type Of Business', required='True')
    tentative_start_date = fields.Date(string='Tentative Start Date', required='True')
    remarks = fields.Text(string='Remarks')
    previous_policy_number = fields.Char(string='Previous Policy Number')
    previous_insurer = fields.Selection(
        selection=[],
        string='Previous Insurer')
    percentage = fields.Char(string='Percentage', required=True)
    policy_name = fields.Selection(
        selection=[],
        string='Policy Name')
    first_followup_date = fields.Datetime(string='First Followup Date', required='True')
    previous_insurer_branch = fields.Selection(
        selection=[],
        string='Previous Insurer Branch')

    @api.onchange('client')
    def _onchange_client(self):
        if self.client:
            self.phone_number = self.client.phone
            self.address = self.client.address
            self.email = self.client.email
            self.contact_person_name = self.client.contact_person_name
            self.designation = self.client.designation
            self.contact_person_phone = self.client.contact_person_phone
            self.contact_person_email = self.client.contact_person_email

