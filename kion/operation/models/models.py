# -*- coding: utf-8 -*-

from odoo import api, Command, fields, models, _
from datetime import date, datetime, time


class operation(models.Model):
    _name = 'operation.operation'
    _description = 'طلب تامين مسؤوليه مدنيه '
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    name = fields.Char(string='أسم طالب التامين ')
    address = fields.Char(string='العنوان')
    activity = fields.Char(string='النشاط')
    from_data = fields.Datetime(string='مده التامين من ')
    to_data = fields.Datetime(string='مده التامين الي ')
    topic = fields.Char(string='أذكر بالتفصيل الأعمال أو النشاط موضوع هذا التأمين  ')
    topic2 = fields.Char(
        string='أذكر الأماكن التى يمارس فيها طالب التأمين الأعمال أو النشاط موضوع هذا التأمين و عدد المواقع   ')
    topic3 = fields.Char(string=' ما هى الآلات والمعدات والأجهزة التى تستخدم فى أداء هذه الأعمال أو النشاط  ')
    topic4 = fields.Char(string=' ما هى الآلات والمعدات والأجهزة التى تستخدم فى أداء هذه الأعمال أو النشاط  ')
    topic5 = fields.Char(string='5- أذكر حدود التعويض المطلوبة للغير للمسئوليه المدنيه عن :', readonly=True)
    topic6 = fields.Char(string='   أ – الإصابات الجسمانية بما فى ذلك الوفاة للشخص الواحد   ')
    topic7 = fields.Char(string='   ب- الإصابات الجسمانية فى الحادث الواحد   ')
    topic8 = fields.Char(string=' ج- الأضرار المادية فى الحادث الواحد   ')
    topic9 = fields.Char(string=' د- الأضرار المادية والجسمانية معاً وخلال مدة التأمين   ')
    topic10 = fields.Char(string=' د- اهل لديك تأمين سارى من المسئولية المدنية قبل الغير    ')
    topic11 = fields.Char(string=' هل سبق لك التأمين على المسئولية المدنية من قبل ؟ ولدى أى شركة    ')
    topic12 = fields.Char(string='  هل سبق أن ألغت لك أى شركة هذا التأمين وما سبب ذلك   ')
    topic13 = fields.Char(string=' 7- أذكر حدود التعويض المطلوبة لمسئوليه السيارات عن  ', readonly=True)
    topic14 = fields.Char(string=' أ-الاصابات الجسمانيه بما في ذلك الوفاة للشخص الواحد')
    topic15 = fields.Char(string='ب- الإصابات الجسمانية فى الحادث الواحد  ')
    topic16 = fields.Char(string='  ج- الأضرار المادية فى الحادث الواحد  ')
    topic17 = fields.Char(string='   د- الأضرار المادية والجسمانية معاً وخلال مدة التأمين    ')
    topic18 = fields.Char(string=' - أذكر حدود التعويض المطلوبة لرب العمل  عن  ', readonly=True)
    topic19 = fields.Char(string='أ-الإصابات الجسمانية بما فى ذلك الوفاة للشخص الواحد   ')
    topic20 = fields.Char(string='ب- الإصابات الجسمانية فى الحادث الواحد  ')
    topic21 = fields.Char(string='  ج- الإصابات الجسمانية خلال مده التأمين  ')
    topic22 = fields.Char(string='د- عدد العمال  ')
    topic23 = fields.Char(string='ذ- اجمالى الرواتب خلال العام  ')
    topic24 = fields.Char(
        string='- أذكر تفاصيل الحوادث التى وقعت للغير بسبب الأعمال أو النشاط الذى تقوم به خلال الثلاثة سنوات الأخيرة ')
    topic25 = fields.Char(string='د- عدد العمال  ')
    topic26 = fields.Binary(string='ارفاق مرفق  ')

    value = fields.Float(string='cost')
    type_of_insurance = fields.Selection(
        [('1', ' طلب تامين مسؤولية مدنية '), ('2', 'طلب تأمين نقل نقدية'), ('3', 'طلب تامين نقل بحري وجوي ')
            , ('4', 'طلب تامين نقل برئ')
            , ('5', 'طلب تامين الحوادث الشخصية ')
            , ('6', 'طلب تامين مسؤوليه رب العمل ')
            , ('7', 'طلب تامبن house hold')
            , ('8', 'طلب تامين اجسام سفن')
            , ('9', 'طلب تامين الحريق')], string='type of insurance:')

    insurance_company_id = fields.Many2many('res.partner', string='company name')
    email_id = fields.Char(string='Insurance company Email')
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    state = fields.Selection(
        [('create', 'create'), ('confirm', 'Confirmed'), ('send_email', 'Send Email'), ('select_offer', 'Select Offer'),
         ('end_mail', 'End Mail'),
         ('cancel', 'Canceled')], string='state', default='create')





    def action_confirm(self):
        self.state = 'confirm'
        action = self.env.ref('operation.action_window')
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Click here',
                'message': '%s',
                'target': 'new',

                'links': [{
                    'label': self.name,
                    'url': f'#action={action.id}&id={self.id}&model=operation.operation &view_type=form'
                }],
                'sticky': True,
            }
        }
        print(self.id)
        return notification



    def send_user_order(self):
        template_id = self.env.ref('operation.mail_template_bib')
        attachment = self.topic26  # Get the binary field value
        attachment_name = 'attachment_filename.ext'  # Set the attachment file name

        # Send the email with the attachment
        all_eamils = self.insurance_company_id
        for email in all_eamils:
            template = self.env.ref('operation.mail_template_bib')
            template.write({'email_to': email.email})
            self.env['mail.template'].browse(template_id.id).send_mail(
                self.id, force_send=True,
                email_values={'attachment_ids': [(0, 0, {
                    'name': attachment_name,
                    'datas': attachment,
                    'type': 'binary'
                })]}
            )





        self.state = 'send_email'
        message = 'The message has been sent successfully'

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'target': 'new',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }




        # all_eamils = self.insurance_company_id
        # for rec in self:
        #
        #     for email in all_eamils:
        #         template = self.env.ref('operation.mail_template_bib')
        #         template.write({'email_to': email.email})
        #         template.send_mail(rec.id, force_send=True)
        #
        #
        #
        #         rec.state = 'send_email'
        #
        #
        #
        #         message = 'The message has been sent successfully'
        #
        #         return {
        #             'type': 'ir.actions.client',
        #             'tag': 'display_notification',
        #             'target': 'new',
        #             'params': {
        #                 'message': message,
        #                 'type': 'success',
        #                 'sticky': False,
        #                 'next': {'type': 'ir.actions.act_window_close'},
        #             }
        #         }
        #

    def select_offer(self):
        for rec in self:
            rec.state = 'select_offer'
            return {
                'name': "select offer",
                'type': 'ir.actions.act_window',
                'view_type': 'tree',
                'view_mode': 'tree',
                'res_model': 'mail.message',
                'view_id': self.env.ref('prt_mail_messages.prt_mail_message_tree').id,

            }

    def end_mail(self):
        for rec in self:
            rec.state = 'end_mail'

            activity_ids = self.mapped('activity_ids').ids
            # Mark the activities as done
            activities = self.env['mail.activity'].browse(activity_ids)
            activities.action_done()

    def cancel_operation(self):
        for rec in self:
            rec.state = 'cancel'


class Specialist(models.Model):
    _name = 'specialist.model'
    _inherit = 'operation.operation'
    # name = fields.Char(compute='get_allvalue')
    # def get_allvalue(self):
    #     valuess=self.env['operation.operation'].search('state','=','confirm')
    #     self.name=valuess.name
    #
