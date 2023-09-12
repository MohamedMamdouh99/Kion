from odoo import api, Command, fields, models, _


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    attachment_files = fields.Many2many('ir.attachment', string='Attachments',
                                        relation='operation_activity_attachment_rel')
    date_deadlinee = fields.Date(default=lambda self: fields.Date.today(), string='Due Date')
    assigned_user_ids = fields.Many2many(
        'res.users',
        'assigned_users_rel',
        'activity_id',
        'user_id',
        string="Assigned Users"
    )
    cc_user_ids = fields.Many2many(
        'res.users',
        'cc_users_rel',
        'activity_id',
        'user_id',
        string="CC"
    )

    activity_body = fields.Text()

    def send_user_email(self):
        template_id = self.env.ref('operation.mail_template_user')
        for email in self.assigned_user_ids:
            template_id.write({'email_to': email.email})
            if self.cc_user_ids:
                cc_emails = [cc.email for cc in self.cc_user_ids]
                template_id.write({'email_cc': ','.join(cc_emails)})

            if template_id:
                template_id.send_mail(self.id, force_send=True)
                self.action_close_dialog()
