from odoo import fields, models, api


class Client(models.Model):
    _name = 'client'
    _description = 'Description'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    image = fields.Image(string='Image')

    contact_person_name = fields.Char(string='Contact Person Name')
    designation = fields.Char(string='Designation')
    contact_person_phone = fields.Char(string='Phone')
    contact_person_email = fields.Char(string='Email')



