from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError, AccessDenied, AccessError, MissingError, ValidationError
from datetime import datetime, timedelta
from odoo.addons.base.models.ir_qweb_fields import nl2br
from jinja2 import Environment, select_autoescape
from odoo import http
from odoo.http import request, route
from datetime import datetime


class AccidentInsurance(models.Model):
    _name = 'accident.insurance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'طلب تأمين من الحوادث الشخصية'
    name = fields.Char(string='اسم طالب التـأمين', tracking=True, required=True, )
    topic1 = fields.Char(string='صلته بالمؤمن عليه ', tracking=True, )
    topic2 = fields.Char(string='الأســـــــــم  ', tracking=True, )
    topic3 = fields.Char(string='البطاقـــــــة : رقم ', tracking=True, )
    topic4 = fields.Date(string='بتاريخ ', tracking=True, )
    topic5 = fields.Char(string='مكتب السجل المدني ', tracking=True, )
    topic6 = fields.Char(string='النشاط الذي يزاوله وطبيعة عمله  ', tracking=True, )
    topic7 = fields.Char(string='فتـــرة مزاولــة هذا النشـــــــــاط  ', tracking=True, )
    topic8 = fields.Char(string='إجمالي الدخل السنوي الذي يحصل عليه  ', tracking=True, )
    topic9 = fields.Char(string='(متوسط السنتين الأخيرتين)  ', tracking=True, )
    topic10 = fields.Char(string='محــــــل الإقـــــامـــــــــــة  ', tracking=True, )
    topic11 = fields.Char(string='محــــــل العمــــــــــــــــــل  ', tracking=True, )

    topic12 = fields.Char(string='اســــــــم الشـــركــــــــــة  ', tracking=True, )
    topic13 = fields.Datetime(string='المـــــــــــــدة : مـــــــــن   ', tracking=True, )
    topic14 = fields.Datetime(string='إلى ', tracking=True, )
    topic15 = fields.Char(string='المستفيــــــــــديــــــــــــن   ', tracking=True, )
    topic16 = fields.Char(string='مبـــــــــــــالغ التـــــأميـن  ', tracking=True, )
    topic17 = fields.Char(string='اســــــــم شـــركـة التأمين ', tracking=True, )
    topic18 = fields.Char(string='مبـــــــــــــالغ التـــــأميـن   ', tracking=True, )
    topic19 = fields.Char(string='فـــــــي حالـــــــة الــوفــــــاة            ', tracking=True, )
    topic20 = fields.Char(string='في حالة العجز الكلي المستديم          ', tracking=True, )
    topic21 = fields.Datetime(string='- مـــــــدة التــــــــأمـــين من   ', tracking=True, )
    topic22 = fields.Datetime(string='إلى')
    topic23 = fields.Datetime(string=' - إذا كان أحد هذه التأمينات قد ألغيت فيوضح تاريخ   ', tracking=True, )
    topic26 = fields.Char(string='  سبب الإلغاء  ', tracking=True, )

    topic24 = fields.Char(string=' هل سبق أن أصبت بحادث تاريخـــه وظروفــــه  ', tracking=True, )
    topic25 = fields.Char(string=' - نتــــــائجــــــــــــــــه   ', tracking=True, )
    topic27 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string='  هل تعاني من أي عيب أو تشـــوه خلقـــي   ',
                               tracking=True)
    topic28 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string='   هل تتلقى في الوقت الحالي أي علاج طبي   ',
                               tracking=True)

    topic29 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' - حمى روماتيزمية، ضغط دم عالي اضطرابات في القلب',
                               tracking=True)
    topic30 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic31 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' - ربو، التهاب رئوي، أمراض صدريه', tracking=True)
    topic32 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic33 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' - صــرع ، نوبــات غيــــاب للوعـــــي',
                               tracking=True)
    topic34 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic35 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' مــــــــــــــرض الســــــــــــــــــــكر',
                               tracking=True)
    topic36 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic37 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' - روماتيزم أو التهــــاب المفاصـــــل',
                               tracking=True)
    topic38 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic39 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' -انزلاق غضروفي أو مشاكل بالظهر', tracking=True)
    topic40 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic41 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' - عـيــــوب فـــي النظـــر أو السمـــع',
                               tracking=True)
    topic42 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic43 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' - انهيار عصبي- ضغط نفسي، اكتئاب', tracking=True)
    topic44 = fields.Char(string='  التفاصيل في حالة الإجابة بنعم ', tracking=True)

    topic45 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' هل تدخن حالياً أو تتناول المشروبات الكحولية ',
                               tracking=True)

    topic46 = fields.Selection([('1', 'نعم'), ('0', 'لا')], string=' -هل سبق أن أصبت بمرض أو عاهة ', tracking=True)
    topic47 = fields.Char(string='  - نــوع المــــرض أو العــاهــــة  ', tracking=True)
    topic48 = fields.Datetime(string=' - تـــــــــــاريــــــــخ ذلــــــــــــك   ', tracking=True)
    topic49 = fields.Char(string=' تفاصيل تطور المرض أو العاهة استمرارا أو استقـرارا أو شفـــاءا  ', tracking=True)

    topic50 = fields.Char(string='   هل تستخدم لأداء واجبات عملك آلات ميكانيكية أو يدوية  ', tracking=True)
    topic51 = fields.Char(string=' هل تتعرض أو تستخدم تيار كهربائي ذو ضغط عالــــي  ', tracking=True)
    topic52 = fields.Char(string='     أو متوسط أو مواد خطرة أو إشعاعات أو مواد ملتهبـــة ', tracking=True)
    topic53 = fields.Char(string='     أو متفجرات أو أوعية ضغط ')
    topic54 = fields.Char(string=' هل يتضمـــــــــن عمــــلك استعمــــــــال السقــــــــالات ', tracking=True)
    topic55 = fields.Char(string='   - هل يتضمن النشاط الذي تعمل به إنشاء الكباري أو المباني ', tracking=True)
    topic56 = fields.Char(string=' أو الأقبية أو الأنفاق أو العمل في الإسطبلات أو المناجم أو      ', tracking=True)
    topic57 = fields.Char(string='    المحاجر أو حفر الآبار  ')
    topic58 = fields.Char(string='  - هل تمارس قيادة الموتوسيكلات البرية أو البحريــــــــــــة  ', tracking=True)
    topic59 = fields.Char(string='  - ما هي أنواع الرياضات التي تزاولها – تذكر بالتفصيــــل  ', tracking=True)

    topic60 = fields.Char(string='  مبلـــــــــــغ التـــــــــــأميــن المطلـــــــــــوب  ', tracking=True)
    topic61 = fields.Char(string=' -   في حالــــــة الوفـــــــــــــــــاة   ', tracking=True)
    topic62 = fields.Char(string=' في حالة العجز الكلي المستديم  ', tracking=True)
    topic63 = fields.Char(
        string=' هل ترغب في تغطية العجز الكلي المؤقت بواقع 5 (في الألف) اسبوعياً من مبلغ التأمين في حالة العجزالمستديم وبحد أقصى لمدة 52 أسبوعاً. ',
        tracking=True)
    topic64 = fields.Char(string=' مبالغ تأمينات وثائق الحياة والحوادث الشخصيـــــة الأخـــرى الســـاريــــــة ',
                          tracking=True)

    topic65 = fields.Char(string=' الاسم بالكامـــــل  ', tracking=True)
    topic66 = fields.Char(string='  الصـــــــــــــــلة   ', tracking=True)
    topic67 = fields.Char(string='  العنـــــــــــــوان   ', tracking=True)
    topic68 = fields.Char(string=' سريان التأميـــن :  المدة   ', tracking=True)
    topic69 = fields.Datetime(string=' من  ', tracking=True)
    topic70 = fields.Datetime(string=' إلى   ', tracking=True)

    topic71 = fields.Char(string='الاســـــــــــم   ', tracking=True)
    topic72 = fields.Char(string='  الوظيفـــــــة   ', tracking=True)
    topic73 = fields.Char(string=' رقم البطاقـة  ', tracking=True)
    topic74 = fields.Char(string=' العنـــــــوان   ', tracking=True)
    topic75 = fields.Datetime(string='تحريراً في:          ', tracking=True)

    relationallll = fields.Many2one('mail.message', string='selected MAil', tracking=True)

    _rec_name = 'name'

    file = fields.Binary(string='ارفاق مرفق  ', tracking=True)
    insurance_company_id = fields.Many2many('res.partner', string='To', tracking=True)

    note22 = fields.Text(string='add Note', tracking=True)

    active = fields.Boolean(string='Active', default=True, tracking=True)

    state = fields.Selection(
        [('create', 'create'), ('confirm', 'Confirmed'), ('send_email', 'the email has been sent '),
         ('select_offer', 'Offer has benn Selected'),
         ('end_mail', 'End Mail'),
         ('cancel', 'Canceled')], string='state', default='create')

    state2 = fields.Selection(
        [('increase', 'Increased'), ('modify', 'Modified'), ('decrease', 'Decreased')], string='state2')

    body_template = fields.Text(string='Body', tracking=True)
    attachment_files_ids = fields.Many2many('ir.attachment', string='Attachments')
    partner_id = fields.Many2one('res.partner', string='CC')
    subject = fields.Char(string="Subject")
    worksheet = fields.Binary(attachment=True, string='رفع الوثيقة')

    add_claims_notes = fields.Text(string='اضافة ملاحظات ')
    add_claims_notes2 = fields.Text(string='اضافة ملاحظات ')

    multiple_files = fields.Binary(string='رفع ملف ')

    before_fix_claims = fields.Many2many('claims.model', string='  طلب معاينة قبل الاصلاح   ')

    after_fix_claims = fields.Many2many('after.fix', string=' طلب معاينه بعد الاصلاح ')

    car_claims = fields.Many2many('car.model', string=' اذن دخول سيارات ')

    client_claims = fields.Many2many('client.document', string='طلب وثيقة عميل ')

    exit_permission_claims = fields.Many2many('exit.permission', string='اذن خروج')

    equal_claims = fields.Many2many('equal.model', string=' نموذج تسوية ')

    # dddddddddddddddddddddddddddddddddd

    def open_pdf(self):

        obj = self.env['mail.message'].search([('id', '=', self.relationallll.id)])
        print(obj.attachment_ids)

        # Replace 'path_to_your_pdf.pdf' with the actual path to your PDF file

        pdf_path = 'path_to_your_pdf.pdf'

        # Generate the URL to open the PDF
        url = '/web/content/%s?' % obj.attachment_ids.id

        # Return an action to open the URL
        return {
            'type': 'ir.actions.act_url',
            'name': 'Open PDF',
            'url': url,
            'target': 'new',
        }

    date_field = fields.Date(default=lambda self: fields.Date.today(), string='Date')

    # def action_close_dialog(self):
    #     print("wq")

    def action_confirm(self):
        self.state = 'confirm'
        action = self.env["ir.actions.actions"]._for_xml_id("operation.my_action_mail_activity_popup")
        action['context'] = {
            'form_view_initial_mode': 'edit',
            'default_res_model_id': self.env.ref('operation.model_accident_insurance').id,
            'default_res_id': self.id,
            'default_date_deadline': fields.Date.to_string(fields.Date.today()),
        }
        return action
        # 'type': 'ir.actions.act_window',
        # 'view_type': 'form',
        # 'view_id': self.env.ref('operation.operation_activity_view_form_popup').id,
        # 'view_mode': 'form',
        # 'res_model': 'mail.activity',
        # 'views': [(False, 'form')],
        # 'target': 'new',
        # 'context': {'form_view_initial_mode': 'edit'}

        # action = self.env.ref('operation.accident_insurance_model_action')
        # notification = {
        #     'type': 'ir.actions.client',
        #     'tag': 'display_notification',
        #     'params': {
        #         'title': 'Click here',
        #         'message': '%s',
        #         'target': 'new',
        #
        #         'links': [{
        #             'label': self.name,
        #             'url': f'#action={action.id}&id={self.id}&model=accident.insurance &view_type=form'
        #         }],
        #         'sticky': True,
        #     }
        # }
        # print(self.id)
        # return notification

    def send_user_order(self):

        for rec in self:

            all_eamils = self.insurance_company_id
            print(all_eamils)
            email_subject = rec.subject

            # fixed_line = "This is a line of words that will appear in every email.\n"
            # email_body = fixed_line + rec.body_template

            print(self.env.user.email)
            if all_eamils:

                for emails in all_eamils:
                    mail_template = self.env.ref('operation.mail_template42_bib')
                    mail_template.write({'email_to': emails.email})
                    attachments = self.attachment_files_ids

                    attachment = self.file  # Get the binary field value
                    attachment_name = 'attachment_filename.ext'  # Set the attachment file name
                    # Send the email with the attachment

                    # Render the template
                    env = Environment(autoescape=select_autoescape(['html', 'xml']))
                    email_body = 'email has been sent successfully'

                    mail_template.send_mail(
                        self.id,
                        force_send=True,
                        email_values={
                            'attachment_ids': [(6, 0, attachments.ids)],
                            'subject': email_subject,

                        }
                    )
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

    def select_offer(self):
        return {
            'name': 'Select Offer',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mail.message',
            'view_id': False,
            'views': [(self.env.ref('prt_mail_messages.prt_mail_message_tree').id, 'tree'),
                      (self.env.ref('prt_mail_messages.prt_mail_message_form').id, 'form')],
            'context': "{'type':'out_invoice'}",
            'type': 'ir.actions.act_window',
            'domain': [('shared_inbox', '=', True)],

        }

    def end_mail(self):
        attachments = self.attachment_files_ids

        obj = self.env['mail.message'].search([('id', '=', self.relationallll.id)])
        object = self.env['mail.message'].search([('id', '=', self.relationallll.id)]).id
        print(object)
        print(obj)
        print(obj.author_allowed_id.id)
        subject = obj.subject
        body = self.note22

        # Create a new mail.mail record
        mail_mail = self.env['mail.mail'].sudo()
        vals = {
            'res_id': object,
            'subject': subject,
            'body_html': body,
            'email_from': self.env.user.work_email,
            'email_to': obj.author_allowed_id.email,
            'reply_to': obj.author_allowed_id.email,
            'attachment_ids': [(6, 0, attachments.ids)],

        }
        mail_id = mail_mail.create(vals)

        # Send the email
        if mail_id:
            mail_id.send()
            print("donnne")
            for rec in self:
                rec.state = 'end_mail'

                activity_ids = self.mapped('activity_ids').ids
                # Mark the activities as done
                activities = self.env['mail.activity'].browse(activity_ids)

                activities.action_done()

    def cancel_operation(self):
        for rec in self:
            rec.state = 'cancel'

    def open_offer(self):
        object = self.env['mail.message'].search([('id', '=', self.relationallll.id)]).id

        return {
            'name': self.name,
            'res_model': 'mail.message',
            'type': 'ir.actions.act_window',
            'res_id': object,
            'context': {},
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(self.env.ref('prt_mail_messages.prt_mail_message_form').id, 'form')],
            'view_id': self.env.ref('prt_mail_messages.prt_mail_message_form').id,
            'target': 'new', }

    def increase(self):
        self.state = 'select_offer'
        self.state2 = 'increase'

    def modify(self):
        self.state = 'select_offer'

        self.state2 = 'modify'

    def decrease(self):
        self.state = 'select_offer'

        self.state2 = 'decrease'

    def renew(self):
        self.state = 'confirm'

    def unlink(self):
        for rec in self:
            if rec.state == 'end_mail':
                raise UserError(_("you cannot delete this policy"))
            else:
                return super(AccidentInsurance, self).unlink()

    def cancel_police(self):
        for rec in self:
            rec.state = 'cancel'

    def open_send_to_form_view(self):
        form_view_id = self.env.ref('operation.accident_insurance_send_to_form_view').id
        return {
            'name': 'Send To Form',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'accident.insurance',
            'res_id': self.id,
            'view_id': form_view_id,
            'target': 'new',  # Opens the form in a new window
        }


    # def send_user_email(self):
    #     template_id = self.env.ref('operation.mail_template_user')  # Replace 'your_module' with your actual module name
    #     template_id.write({'email_to': self.assigned_user_ids.email})
    #     if template_id:
    #         template_id.send_mail(self.id, force_send=True)

    # def two_methods(self):
    #     self.action_confirm()
    #     self.send_user_order()
