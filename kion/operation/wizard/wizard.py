from odoo import models, fields, api

class PopoWizard(models.TransientModel):
    _name="pop.wizard.cancel"
    values=fields.Char(string="enter name")

    def clickk(self):
        passs=self.env.user
        print(passs)