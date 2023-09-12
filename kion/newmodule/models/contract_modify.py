from odoo import models, fields, api
import requests
from datetime import datetime, timedelta
import time


class ContractModify(models.Model):
    _inherit = 'hr.contract'
    medical_insurancee = fields.Float(string='Medical Insurance')
    mobile_allowance = fields.Float(string='Mobile Allowance')
    transportation_allowance = fields.Float(string='Transportation Allowance')
    social_allowance = fields.Float(string='Social Allowance')

    new_state = fields.Selection([('expulsion', 'expulsion'), ('resignation', 'resignation')], string='state')
    state_newvalue = fields.Char(string='contract_states', stored=True)

    @api.onchange('new_state')
    def _onchange_state(self):
        if self.new_state == 'expulsion':
            self.state_newvalue = 'expulsion'
            print(self.state_newvalue)
        elif self.new_state == 'resignation':
            self.state_newvalue = 'resignation'
            print(self.state_newvalue)

        else:
            print('hi')


class ContractModifyHistory(models.Model):
    _inherit = 'hr.contract.history'
    state_newvalue = fields.Char(string='contract_states')


    # def get_state_value(self):

    #     value = self.env['hr.contract'].search([('employee_id.id', '=', self.employee_id.id)]).state_newvalue
    #     if value=='expulsion':
    #         print(value)
    #     elif value=='resignation':
    #         print(value)
    #     else:
    #         print('not found')
    #

#
# def attendance_log(self):
#     i = 0
#     last_date = self.env['hr.attendance'].search([], limit=1, order='check_in desc')
#     if last_date:
#         last_d = last_date.check_in + timedelta(days=1)
#         from_date = last_d.strftime("%Y-%m-%d")
#         to_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
#         r = requests.get('http://192.168.1.111:12100/api/Sap/getsap/?fromdate=' + from_date + '&todate=' + to_date,
#                          verify=False)
#         print("from => ", from_date, "   to => ", to_date)
#     else:
#         r = requests.get('http://192.168.1.111:12100/api/Sap/getsap/', verify=False)
#     data = r.json()
#     if self.env['ir.cron'].search([('name', '=', "Repro: Automatic Attendance Log")]).old_att:
#         data = eval(self.env['ir.cron'].search([('name', '=', "Repro: Automatic Attendance Log")]).old_att)
#     for lp_rec in data:
#         checkin_ls = []
#         checkout_ls = []
#         emp_id = self.env['hr.employee'].search([('device_id', '=', int(lp_rec['AC-No']))])
#         if emp_id:
#             for i in data:
#                 if i['AC-No'] == lp_rec['AC-No']:
#                     in_t = str(lp_rec['date']) + ' ' + time.strftime(lp_rec['timein'] + ':00')
#                     out_t = str(lp_rec['date']) + ' ' + time.strftime(lp_rec['timeout'] + ':00')
#                     checkin_ls.append(datetime.strptime(in_t, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2))
#                     checkout_ls.append(datetime.strptime(out_t, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2))
#
#             checkin_ls = sorted(checkin_ls)
#             checkout_ls = sorted(checkout_ls, reverse=True)
#             x = self.env['hr.attendance'].search(
#                 [('device_id', '=', str(lp_rec['AC-No'])),
#                  ('check_in', '=', checkin_ls[0])])
#             if not x:
#                 recc = self.env['hr.attendance'].create({
#                     'device_id': str(lp_rec['AC-No']),
#                     'employee_id': emp_id.id,
#                     'check_in': checkin_ls[0],
#                     'check_out': checkout_ls[0],
#                     'data': data,
#                 })
#                 if checkin_ls[0] == checkout_ls[0]:
#                     recc.write({
#                         'no_checkout': True
#                     })
#
#     # for one_record in data[0]:
#     #     emp_id = self.env['hr.employee'].search([('ivf_emp_no', '=', str(one_record['empCode']))])
#     #     if emp_id:
#     #         print('Found', emp_id)
#     #         x = str(one_record['date']) + ' ' + time.strftime(one_record['timein'] + ':00')
#     #         y = str(one_record['date']) + ' ' + time.strftime(one_record['timeout'] + ':00')
#     #         print(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2))
#     #
#     #         rec.env['hr.attendance'].create({
#     #             'ivf_emp_no': str(one_record['empCode']),
#     #             'employee_id': emp_id.id,
#     #             'check_in': datetime.strptime(x, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2),
#     #             'check_out': datetime.strptime(y, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2)
#     #         })
#     #
#     #         check_in_ls.sort()
#     #         check_out_ls.sort(reverse=True)
#
#     # for rec in self:
#     #     while i < len(data):
#     #         emp_id = rec.env['hr.employee'].search([('ivf_emp_no', '=', str(data[i]['empCode']))])
#     #         print('Found', emp_id)
#     #         if emp_id:
#     #             x = str(data[i]['date']) + ' ' + time.strftime(data[i]['timein'] + ':00')
#     #             y = str(data[i]['date']) + ' ' + time.strftime(data[i]['timeout'] + ':00')
#     #             print(datetime.strptime(x, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2))
#     #             # Create Record in Attendance
#     #
#     #             # => To Press log multiple times without creating duplicated records
#     #             # for record in self.env['hr.attendance'].search([]):
#     #             #
#     #             #     if record.employee_id == emp_id.id and record.check_in == datetime.strptime(x,
#     #             #                                                                                 "%Y-%m-%d %H:%M:%S") + timedelta(
#     #             #         hours=-2) and record.check_out == datetime.strptime(y, "%Y-%m-%d %H:%M:%S") + timedelta(
#     #             #         hours=-2):
#     #             #         break
#     #             #     else:
#     #
#     #             rec.env['hr.attendance'].create({
#     #                 'ivf_emp_no': str(data[i]['empCode']),
#     #                 'employee_id': emp_id.id,
#     #                 'check_in': datetime.strptime(x, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2),
#     #                 'check_out': datetime.strptime(y, "%Y-%m-%d %H:%M:%S") + timedelta(hours=-2)
#     #             })
#     #         else:
#     #             pass
#     #         i += 1
#     #         print(i)
#
# # <record model="ir.cron" id="cron_automatic_log">
# #        <field name="name">Repro: Automatic Attendance Log</field>
# #        <field name="model_id" ref="model_hr_attendance"/>
# #        <field name="state">code</field>
# #        <field name="code">model.attendance_log()</field>
# #        <field name="interval_number">24</field>
# #        <field name="interval_type">hours</field>
# #        <field name="numbercall">-1</field>
# #        <field name="nextcall">2022-05-12 21:59:30</field>
# #    </record>
