from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError, AccessDenied, AccessError, MissingError, ValidationError
from datetime import datetime, timedelta


class SeaAirTransport(models.Model):
    _name = 'sea.air.transport'
    _description = 'طلب تأمين نقل بحرى / جوى'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='إسم المؤمن له ')
    topic1 = fields.Char(string='نوع البضاعة ')
    topic2 = fields.Char(string='	طريقة الشحن	')
    topic3 = fields.Char(string='الحجم أو الوزن القائم للرسالة ')
    topic4 = fields.Char(string='مبلغ التأمين')
    topic5 = fields.Char(string='إعتماد مستندى رقم / إستمارة ت.ص رقم ')
    topic6 = fields.Char(string='إسم الباخرة')
    topic7 = fields.Char(string='ميناء الشحن')
    topic8 = fields.Datetime(string='تاريخ الشحن ')
    topic9 = fields.Char(string='ميناء الوصول')
    topic10 = fields.Datetime(string='تاريخ الوصول ')
    topic11 = fields.Char(string='الرحلـة من')
    topic12 = fields.Char(string='إلى')
    topic13 = fields.Char(string='إسم المورد / إسم المرسل إليه ')
    topic14 = fields.Char(string='قيمة الرسالة ')
    topic15 = fields.Char(string='الأخطار المؤمن ضدها : شروط المجمع لتأمين البضائع ( أ ) أو ( ج ) أو (فقد كلى)')
    topic16 = fields.Char(string='شروط المجمع لتأمين الحرب والإضرابات (بضائع) – التأمين ضد أخطار الحروب')
    topic17 = fields.Char(string='ملاحظـات ')
    topic18 = fields.Char(string='إقرار')
    topic19 = fields.Char(string='نرغب فى إبرام هذا التأمين مع المجموعة العربية المصرية للتأمين طبقا لما ذكر اعلاه ، ونقر نحن الموقعين ادناه ان جميع البيانات الواردة فى هذا الطلب صحيحة وتطابق الواقع واننا لم نخف عن الشركة اى من البيانات المتعلقة بالأخطار المراد التأمين عليها ونوافق على ان يكون هذا الطلب اساسا لعقد التأمين يبدأ سريان هذا التأمين بمجرد قبول الشركة لهذا الطلب وبعد قيامكم بسداد القسط المطلوب')
    topic20 = fields.Datetime(string='التاريخ       /    /       ')
    topic21 = fields.Char(string='توقيع طالب التأمين')





    _rec_name = 'name'


    file = fields.Binary(string='ارفاق مرفق  ')
    insurance_company_id = fields.Many2many('res.partner', string='company name')


    file2 = fields.Binary(string='ارفاق مرفق  ')
    note22=fields.Text(string='add Note')






    state = fields.Selection(
        [('create', 'create'), ('confirm', 'Confirmed'), ('send_email', 'Send Email'), ('select_offer', 'Select Offer'),
         ('end_mail', 'End Mail'),
         ('cancel', 'Canceled')], string='state', default='create')


    def action_confirm(self):
        self.state = 'confirm'
        action = self.env.ref('operation.sea_and_air_model_action')
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Click here',
                'message': '%s',
                'target': 'new',

                'links': [{
                    'label': self.name,
                    'url': f'#action={action.id}&id={self.id}&model=sea.air.transport &view_type=form'
                }],
                'sticky': True,
            }
        }
        print(self.id)
        return notification


    def send_user_order(self):
        template_id = self.env.ref('operation.mail_template2_bib')
        attachment = self.file  # Get the binary field value
        attachment_name = 'attachment_filename.ext'  # Set the attachment file name

        # Send the email with the attachment
        all_eamils = self.insurance_company_id
        if all_eamils:
            for email in all_eamils:
                template = self.env.ref('operation.mail_template1_bib')
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
        else:
            raise UserError(_("you should select email to send mail"))


    def select_offer(self):
        self.state = 'select_offer'
        return {
            'name': 'Select Offer',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mail.message',
            'view_id': False,
            'views': [(self.env.ref('prt_mail_messages.prt_mail_message_tree').id, 'tree'),
                      (self.env.ref('prt_mail_messages.prt_mail_message_form').id, 'form')],
            'context': "{'type':'out_invoice'}",
            'type': 'ir.actions.act_window'
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
