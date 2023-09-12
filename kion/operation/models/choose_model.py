from odoo import api, Command, fields, models, _



class ChooseModel(models.Model):
    _name = 'choose.model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    type_of_insurance = fields.Selection(
        [('1', ' طلب تامين مسؤولية مدنية '), ('2', 'طلب تأمين نقل نقدية'), ('3', 'طلب تامين نقل بحري وجوي ')
            , ('4', 'طلب تامين نقل برئ')
            , ('5', 'طلب تامين الحوادث الشخصية ')
            , ('6', 'طلب تامين مسؤوليه رب العمل ')
            , ('7', 'طلب تامبن house hold')
            , ('8', 'طلب تامين اجسام سفن')
            , ('9', 'طلب تامين الحريق')], string='type of insurance:')

    def open_form(self):
        if self.type_of_insurance=='1':
            return {
                'name': "طلب التامين من المسؤولية المدنية ",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'operation.operation',
                'view_id': self.env.ref('operation.form').id,
                'target': 'new'
            }
        elif self.type_of_insurance=='2':
            return {
                'name': "cashtransfer.model",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'cashtransfer.model',
                'view_id': self.env.ref('operation.cashtransfer_model_form_type').id,
                'target': 'new'
            }
        elif self.type_of_insurance=='3':
            return {
                'name': "طلب تأمين نقل بحرى / جوى",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sea.air.transport',
                'view_id': self.env.ref('operation.sea_air_transport_form').id,
                'target': 'new'
            }
        elif self.type_of_insurance=='4':
            return {
                'name': "طلب تأمين نقل بري",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'land.transfer.model',
                'view_id': self.env.ref('operation.land_transfer_form').id,
                'target': 'new'
            }
        elif self.type_of_insurance=='5':
            return {
                'name': "طلب تأمين من الحوادث الشخصية",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'accident.insurance',
                'view_id': self.env.ref('operation.accident_insurance_form').id,
                'target': 'new'
            }
        else:
            print('sorry')
