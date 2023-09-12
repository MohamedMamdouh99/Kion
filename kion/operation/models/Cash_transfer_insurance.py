from odoo import api, Command, fields, models, _
from odoo.exceptions import UserError, AccessDenied, AccessError, MissingError, ValidationError
from datetime import datetime, timedelta



class CashTransfer(models.Model):
    _name = 'cashtransfer.model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'طلب تامين نقل نقدية '
    _rec_name = 'name'
    state = fields.Selection(
        [('create', 'create'), ('confirm', 'Confirmed'), ('send_email', 'Send Email'), ('select_offer', 'Select Offer'),
         ('end_mail', 'End Mail'),
         ('cancel', 'Canceled')], string='state', default='create')

    name = fields.Char(string='اسم الشركة كاملا  ')
    address = fields.Char(string='العنوان – المركز الرئيسي ')
    phone = fields.Char(string='تليفون ')
    phone2 = fields.Integer(string='فاكس  ')
    topic = fields.Char(string='- فروع أخرى ')
    topic2 = fields.Char( string='نوع الشركة ')
    topic3 = fields.Char(string=' هل كانت الشركة تعمل تحت أي مسمي آخر   ')
    topic4 = fields.Char(string=' – حجم – نسبة الأموال المستعملة   ')
    topic5 = fields.Char(string='نشاط الشركة بالتفصيل :')
    topic6 = fields.Datetime(string=' تاريخ بداية التامين المطلوب   ')
    topic7 = fields.Char(string='هل سبق التامين لدي شركات أخرى ؟ ما هي ؟ ')
    topic8 = fields.Char(string='هل سبق وان تم إلغاء وثائق تامين صادرة لصالحكم ؟ متي وأين ؟  ')
    topic9 = fields.Char(string='هل هناك حوادث وقعت خلال الخمس سنوات السابقة - ؟ نرجوا إيضاحها تفصيليا  ؟  ')
    topic10 = fields.Char(string=' د- اهل لديك تأمين سارى من المسئولية المدنية قبل الغير    ')
    names_of_manager=fields.One2many('cashtransfer.model.line', 'relation_field1',string='أسماء المديرين وخبراتهم السابق ')

    topic11 = fields.Char(string=' بعد التحري والتقصي عن الموظفين لديكم .  هل يوجد أي شخص اشترك في حوادث سطو علي سيارة مجهزة ')
    topic101 = fields.Char(string=' عدد الموظفين الدائمين في كل نوع من الأنواع المذكورة  ')
    topic111 = fields.Char(string='هل يوجد عمالة تعمل نصف الوقت ')
    topic12 = fields.Char(string='– هل يشترط أن يخضع جميع العملين الجدد للفحوصات  أ_كشف طبي ب_كاشف الكذب  ج_كشف نفسي ')
    topic13 = fields.Char(string= 'عند تعيين موظف . هل يتم الحصول علي المعلومات التالية  ',readonly=True)
    A = fields.Boolean('الاستفسار عن الموظف عن طريق أماكن عمله السابقة ')
    B = fields.Boolean('البنوك')
    C = fields.Boolean('الجيران ')
    D = fields.Boolean('شهادة مخالفات مرورية ')
    topic14 = fields.Char(string=' هل يتم الاحتفاظ بصور شخصية – فيش وتشبيه للموظفين ')
    topic15 = fields.Char(string='هل يوجد نسخة أخرى من هذه المستندات في مكان آخر  ')
    topic16 = fields.Char(string='هل لجميع العاملين المسلحين في عمليات نقل الأموال زي محدد (ملابس رسمية)؟')
    topic17 = fields.Char(string='– هل يتم تسليم جميع وثائق أو مستندات التعريف في حالة ترك الموظف للخدمة ؟ ')
    topic19 = fields.Char(string='ما هي وسيلة تعرف عملائكم علي ناقلي النقدية ( صور – توقيعات – بطاقة تعريف ) ')

    topic20 = fields.Char(string='هل يوجد برامج تدريب ')
    topic21 = fields.Char(string=' هل يوجد نظام مكتوب لإجراءات العمل ')
    topic22 = fields.Char(string='هل يتم تطبيق نظام التدريب و الإجراءات ')
    topic23 = fields.Char(string=' ما هي فترة الاختبار التي يستغرقها الموظف لكي يبدا العمل ')



    topic24 = fields.Char(string='هل مطلوب تغطية هذا الجزء في مباني الشركة  ')
    limite_cost_insurance=fields.One2many('cashtransfer.model.line2', 'relation_field2',string='حدود مبالغ التامين المطلوبة')


    topic25 = fields.Char(string='نقـــديـــــــــــة ')
    topic26 = fields.Char(string='عملات معدنية')
    topic27 = fields.Char(string='طواــــــــــــبع ')
    topic28 = fields.Char(string='أخـــــــــــرى ')

    topic29 = fields.Char(string='هل الحدود القصوى التي تم تحديدها بعالية هي الاحتياطات التي يجب توافرها بسبب متطلبات قانونية  ')

    topic30=fields.One2many('cashtransfer.model.line3', 'relation_field3',string='هل تقوم بأداء عمليات فرز وتجميع النقود والعملات في غرفة عمليات مخصصة لهذا الغرض')
    topic31=fields.One2many('cashtransfer.model.line4', 'relation_field4',string='وصف للغرف المحصنة / الخزائن في كل مبني -  موقع ')

    topic32=fields.One2many('cashtransfer.model.line5', 'relation_field5',string='– وصف لأنواع أجهزة الإنذار لكل مبني  ')


    topic33 = fields.Char(string='هل يوجد عقد لصيانة أجهزة الإنذار  ')
    topic34 = fields.Char(string='– هل أي شخص يعمل لديكم لديه كافة ألا كواد والإجراءات اللازمة لتشغيل أجهزة إنذار  ')
    topic35 = fields.Char(string=' – هل يتم فتح أو غلق الخزائن و الغرف المحصنة إلا بوجود عدد محدد من الأشخاص  ')

    topic36 = fields.Char(string=' كم مرة يتم تعديل اكواد النظام ونظام فتح الخزائن والغرف المحصنة  ')
    topic37 = fields.Char(string='هل من المعتاد وجود حراسة طوال أل ساعة يوميا ؟ إذا كانت الإجابة بالنفي اذكر عدد ساعات العمل المعتادة  ')

    topic38 = fields.Char(string=' كم عدد الأشخاص الموجودين في الخدمة أثناء :- ساعات العمل الرسمية المسلحين وغير المسلحين')
    topic39= fields.Char(string=' كم عدد الأشخاص الموجودين في الخدمة أثناء :-غير ساعات العمل الرسمية  ')

    topic40 = fields.Char(string='صف طريقة الدخول لمباني الشركة  ')

    topic41 = fields.Char(string='– هل جميع السيارات المستخدمة في نقل الأموال مجهزة بحاجز خاص أو ساتر يؤدي إلى حماية كاملة لشخص واحد علي الأقل من طاقم السيارة عند فتح أحد أبوابها ؟ في حالة النفي نرجوا شرح التفاصيل الخاصة بهذه النقطة ')
    topic42 = fields.Char(string='ما هو الحد الأدنى لطاقم السيارة الواحدة بخلاف السائق ')
    topic43 = fields.Char(string='عندما تكون السيارة المجهزة غير مؤمنة و / أو ليس عليها حراسة   هل من سياسة الشركة المنفذة أن يوجد علي الأقل شخص واحد من الطاقم داخل السيارة في جميع الأوقات أثناء العمليات ؟ إذا كانت الإجابة بالنفي نرجوا ذكر التفاصيل المتبقية  ')

    topic44=fields.One2many('cashtransfer.model.line6', 'relation_field6',string='– ما هو أقصى مبلغ يحتمل نقله من السيارة إلى الموقع المطلوب ويكون معرض للخطر ( أخطار طريق )  ')



    topic45 = fields.Char(string='نقـــديـــــــــــة ')
    topic46 = fields.Char(string='عملات معدنية')
    topic47 = fields.Char(string='طواــــــــــــبع ')
    topic48 = fields.Char(string='أخـــــــــــرى ')


    topic49 = fields.Selection([('1','اقفال الابواب داخلياا'),('2','طرق اخري')],string='ما هي الإجراءات التي يتم اتخاذها أثناء تواجد النقود أو الأشياء الأخرى داخل السيارة ')

    topic50= fields.Char(string='هل السيارة يحتفظ بها في مكان آمن ومغلق عند عدم استخدامها  ')
    topic51= fields.Char(string='هل يوجد نظام معين للمحافظة علي مفاتيح السيارة  ')
    topic52= fields.Char(string='وصف للأنواع المستخدمة من اللاسلكي ')
    topic53= fields.Char(string='وصف للأنواع المستخدمة من اللاسلكي  ')
    topic54= fields.Char(string='ما هو عدد السيارات المجهزة – المسلحة  في الخدمة ')
    topic55= fields.Char(string=' ما هو عدد السيارات الاحتياطي ')
    topic56= fields.Char(string='هل يتم نقل أموال أو أشياء ثمينة في سيارات غير مجهزة  ')

    topic57= fields.Char(string='برجاء إرفاق كشف بكافة السيارات التي سيتم تامين نقل الأموال التي تقوم بحملها ')
    topic58= fields.Char(string='نرجوا موافاتنا بصورة من عقد نقل الأموال مع أحد عملائكم ')



    topic59= fields.Char(string=' ما هو نوع الخدمة التي تقدمها  ')
    topic60= fields.Char(string='هل يوجد لديك موظف جاهز لتقديم الخدمة طوال أل ساعة  ')
    topic61= fields.Char(string='هل تستخدم سيارات مجهزة لعمليات الصرف الآلي ')
    topic62= fields.Char(string='هل السيارات المخصصة لهذا الغرض تترك بدون حراسة ؟ لماذا ')
    topic63= fields.Char(string='– هل يوجد عدد ( 2 ) مسلح كحد ادني  ')
    topic64= fields.Char(string='هل الماكينات التي تقومون بخدمتها تحتوي علي شرائط لتخزين المعلومات ')
    topic65= fields.Char(string='ما هي الجهات التي يتم التعامل معها – استلام النقود والاشياء الثمينة لتوصيلها ')
    topic66= fields.Char(string='هل يتم استلام النقود لتوصيلها في نفس اليوم ؟ ام يمكن الاحتفاظ بها لليوم التالي ')

    topic67 = fields.Boolean('هل المؤمن له مواطن يحمل الجنسيه الامريكيه وجنسيه اخرى .. مزدوج الجنسيه  ')
    topic68 = fields.Boolean('مواطن امريكى مقيم داخل الولايات المتحده   ')
    topic69 = fields.Boolean('ام خارج الولايات المتحده  ')
    topic70 = fields.Boolean('يحمل جواز سفر أمريكى ')
    topic71 = fields.Boolean('مولود فى الولايات المتحدة الأمريكية ولم يتخل عن الجنسيه الامريكيه ')
    topic72 = fields.Boolean(' مقيم إقامة دائمة وبصورة شرعية بالولايات المتحده الامريكيه ( أى حامل الإقامة الدائمة Green Card) .')
    topic73 = fields.Boolean('خاضع لإختبار حضور جوهرى، ويقصد به المقيم غير الأمريكى الموجود فى الولايات المتحدة الأمريكية منذ 183 يوماً كحد أدنى باحتساب كل أيام السنة الحالية، أو قضى ثلث                               الأيام من السنة السابقة مباشرة، أو سدس الأيام فى السنة الثانية ( وليس دبلوماسياً أو محاضراً أو طالباً أو رياضياً )')

    topic74 = fields.Boolean('هل الشركة المؤمن لها شركة امريكيه وتعمل داخل الولايات المتحده الامريكيه   ')
    topic75 = fields.Boolean('هل الشركة المؤمن لها بها شركاء داخل الولايات المتحده الامريكيه  ')
    topic76 = fields.Boolean('هل حجم التعامل يزيد عن 50الف دولار او ما يعادلها من العملات الاخرى  ')

    topic77= fields.Text(string='إقــــــــــرار ')



















    file = fields.Binary(string='ارفاق مرفق  ')
    insurance_company_id = fields.Many2many('res.partner', string='company name')
    partner_id = fields.Many2one('res.partner', string='partner name')
    description=fields.Text(string='add notes')
    policy_note=fields.Text(string='Note')







    def action_confirm(self):
        self.state = 'confirm'
        action = self.env.ref('operation.Cash_transfer_insurance_action')
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Click here',
                'message': '%s',
                'target': 'new',

                'links': [{
                    'label': self.name,
                    'url': f'#action={action.id}&id={self.id}&model=cashtransfer.model &view_type=form'
                }],
                'sticky': True,
            }
        }
        print(self.id)
        return notification


    def send_user_order(self):
        for rec in self:
            template_id = rec.env.ref('operation.mail_template1_bib')
            attachment = rec.file  # Get the binary field value
            attachment_name = 'attachment_filename.ext'  # Set the attachment file name

            # Send the email with the attachment
            all_eamils = rec.insurance_company_id
            if all_eamils:
                for email in all_eamils:
                    template = rec.env.ref('operation.mail_template1_bib')
                    template.write({'email_to': email.email})
                    rec.env['mail.template'].browse(template_id.id).send_mail(
                        rec.id, force_send=True,
                        email_values={'attachment_ids': [(0, 0, {
                            'name': attachment_name,
                            'datas': attachment,
                            'type': 'binary'
                        })]}
                    )

                rec.state = 'send_email'
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




















class Cash_Transfer_Insurance_line(models.Model):
    _name = 'cashtransfer.model.line'

    name=fields.Char(string='الاسم')
    job=fields.Char(string='الوظيفة')
    years=fields.Char(string='عدد سنوات في الشركة')
    experience=fields.Char(string='عدد سنوات الخبره')
    relation_field1 = fields.Many2one('cashtransfer.model')

class Cash_Transfer_Insurance_line2(models.Model):
    _name = 'cashtransfer.model.line2'

    day=fields.Char(string='اليوم')
    limit=fields.Char(string='الحد الأقصى للنقلة')
    numbers=fields.Char(string='عدد المرات خلال الشهر')
    average=fields.Char(string='المتوسط')

    relation_field2 = fields.Many2one('cashtransfer.model')
class Cash_Transfer_Insurance_line3(models.Model):
    _name = 'cashtransfer.model.line3'

    type=fields.Char(string='النوع')
    limit=fields.Char(string='الحد الأقصى')
    numbers=fields.Char(string='عدد المرات خلال الشهر')
    average=fields.Char(string='المتوسط')

    relation_field3 = fields.Many2one('cashtransfer.model')

class Cash_Transfer_Insurance_line4(models.Model):
    _name = 'cashtransfer.model.line4'

    location=fields.Char(string='الموقع')
    job=fields.Char(string='الوظيفة')
    model=fields.Char(string='الموديل')
    doubel_lock=fields.Char(string='القفل المزدوج')
    close_time=fields.Char(string='ساعة الإغلاق')

    relation_field4 = fields.Many2one('cashtransfer.model')


class Cash_Transfer_Insurance_line5(models.Model):
    _name = 'cashtransfer.model.line5'

    code=fields.Char(string='كود الإنذار')
    control_unit=fields.Char(string='وحدة التحكم')
    degree=fields.Char(string='الدرجة')

    relation_field5 = fields.Many2one('cashtransfer.model')


class Cash_Transfer_Insurance_line6(models.Model):
    _name = 'cashtransfer.model.line6'

    day=fields.Char(string='اليوم ')
    limit=fields.Char(string='الحد الأقصى للنقلة ')

    relation_field6 = fields.Many2one('cashtransfer.model')



