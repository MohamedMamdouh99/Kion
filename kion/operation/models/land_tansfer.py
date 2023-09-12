from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError, AccessDenied, AccessError, MissingError, ValidationError
from datetime import datetime, timedelta


class LandTransfer(models.Model):
    _name = 'land.transfer.model'
    _description = 'طلب تأمين نقل بري'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='إسم المؤمن له ')
    topic1 = fields.Char(string='نوع البضاعة ')
    topic2 = fields.Char(string='	مبلغ التأمين	')
    topic3 = fields.Char(string='الحد الأقصى للشحنة ')
    topic4 = fields.Char(string='الأخطار المؤمن عليها: أخطار طريق فقط و (اخطار اضافية أخرى)   ')
    topic5 = fields.Char(string='الرحلة من ')
    topic6 = fields.Char(string='الي')
    topic7 = fields.Char(string='وسيلة النقل : مؤجرة / ملك المؤمن له ')
    topic8 = fields.Datetime(string='تاريخ الشحن ')
    topic9 = fields.Char(string='رقـم السيارة  ')
    topic10 = fields.Char(string='اسم السائق : بطاقة شخصية عائلية  ')
    topic11 = fields.Text(string='ملاحظـات ')

    topic12 = fields.Datetime(string='التاريخ       /    /       ')
    topic13 = fields.Char(string='توقيع طالب التأمين')
    upload_file=fields.Binary(string='ارفاق ملف ')




    topic14 = fields.Char(string='Insured:')
    topic15 = fields.Char(string='Shipment:')
    topic16 = fields.Char(string='Sum insured:')
    topic17 = fields.Char(string='Max. Value per one shipment:  ')
    topic18 = fields.Char(string='Voyage from:   ')
    topic19 = fields.Char(string='Voyage to:')

    topic75 = fields.Boolean('Rent trucks :  ')
    topic76 = fields.Boolean('Rent owned: ')

    topic109 = fields.Char(string='Plate No:')
    topic111 = fields.Char(string='Driver Name:')
    topic112 = fields.Char(string='ID No:')
    topic113 = fields.Char(string='Risks insured:    Road Risk   (and additional Risks):')
    topic114 = fields.Char(string='Notes:')
    topic115 = fields.Datetime(string='Date:')
    topic116 = fields.Char(string='Insureds Signature:')





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
        action = self.env.ref('operation.land_transfer_model_action')
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Click here',
                'message': '%s',
                'target': 'new',

                'links': [{
                    'label': self.name,
                    'url': f'#action={action.id}&id={self.id}&model=land.transfer.model &view_type=form'
                }],
                'sticky': True,
            }
        }
        print(self.id)
        return notification


    def send_user_order(self):
        template_id = self.env.ref('operation.mail_template3_bib')
        attachment = self.file  # Get the binary field value
        attachment_name = 'attachment_filename.ext'  # Set the attachment file name

        # Send the email with the attachment
        all_eamils = self.insurance_company_id
        if all_eamils:
            for email in all_eamils:
                template = self.env.ref('operation.mail_template3_bib')
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
