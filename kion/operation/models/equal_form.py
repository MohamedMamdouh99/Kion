from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError, AccessDenied, AccessError, MissingError, ValidationError
from datetime import datetime, timedelta
from odoo.addons.base.models.ir_qweb_fields import nl2br
from jinja2 import Environment, select_autoescape
from odoo import http
from odoo.http import request, route


class ClaimsModel(models.Model):
    _name = 'equal.model'
    _description='equal form'

    center_name=fields.Char(string='مركز خدمة : ')
    number=fields.Char(string='رقم العميل : ')
    name=fields.Char(string='اسم المالك ')
    topic2=fields.Char(string='نوع السياره ')
    topic3=fields.Char(string='موديل السيارة ')
    topic4=fields.Char(string='سنة الصنع  ')
    topic5=fields.Char(string='رقم الشاسية ')
    topic6=fields.Char(string='رقم اللوحات ')
    topic7=fields.Char(string='شركة التامين ')
    topic8=fields.Char(string='قيمة الفاتوره ')
    topic9=fields.Char(string='رقم الفاتوره ')
    topic10=fields.Char(string='طريقة الدفع ')


    topic11=fields.Char(string='اهلاكات الاجزاء المبكانيكية ')
    topic12=fields.Char(string='اهلاكات الاجزاء العادية ')
    topic13=fields.Char(string='اهلاكات مشتملات الزجاج ')
    topic14=fields.Char(string='اهلاك الكاوتش والجنوط ')
    topic15=fields.Char(string='اهلاك الايرباج والبطارية ')
    topic16=fields.Char(string='شرط الاصلاح بالتوكيل  ')
    topic17=fields.Char(string='تحملات اخري ')
    topic18=fields.Char(string='قطع غيار غير معتمده')
    topic19=fields.Char(string='اجمالي تحميلات العميل  ')
    topic20=fields.Char(string='اجمالي تحميلات  مركز الخدمة')
    topic21=fields.Char(string='تم الارسال عن طريق  ')











    note_sent=fields.Char(string='ملاحظات ')
    attachment_files_ids = fields.Many2many('ir.attachment', string='Attachments')
    _inherit = ['mail.thread', 'mail.activity.mixin']
    choose_partner=fields.Many2many('res.partner' , string='choose email to send ')

    state = fields.Selection(
        [('create', 'create'), ('confirm', 'Confirmed'), ('send_email', 'Done'),
         ('cancel', 'Canceled')], string='state', default='create')


    def action_confirm(self):
        self.state='confirm'


    def send_user_order(self):

        for rec in self:

            all_eamils = self.choose_partner
            print(all_eamils)

            print(self.env.user.email)
            if all_eamils:

                for emails in all_eamils:
                    mail_template = self.env.ref('operation.equal_model_template1dd1')
                    mail_template.write({'email_to': emails.email})
                    attachments = self.attachment_files_ids

                    email_body ='email has been sent successfully'

                    mail_template.send_mail(self.id, force_send=True, email_values={'attachment_ids': [(6, 0, attachments.ids)]})
                    attachment_idss = []
                    for attachment in attachments:
                        attachment_idss.append(attachment.id)

                    self.message_post(
                        body=email_body,
                        subject='Email Content',
                        message_type='email',
                        attachment_ids=attachment_idss

                    )

                    print(emails.email)

                title = _("Successfully!")
                message = _("Your Message has been sent Successfully!")
                rec.state = 'send_email'

                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'target': 'new',

                    'params': {
                        'title': title,
                        'message': message,
                        'sticky': False,
                        'next': {'type': 'ir.actions.act_window_close'},

                    }
                }
            else:
                raise UserError(_("you should select email to send mail"))







    def cancel_operation(self):
        self.state = 'cancel'
