###################################################################################
# 
#    Copyright (C) Cetmix OÜ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER GENERAL PUBLIC LICENSE as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

from .common import MailMessageCommon


class TestMailMessageBase(MailMessageCommon):
    def setUp(self):
        super(TestMailMessageBase, self).setUp()

    def test_get_mail_thread_data_res_partner(self):
        """Test flow get thread data for `res.partner` record"""
        result = self.res_partner_ann._get_mail_thread_data([])
        self.assertTrue(result.get("hasWriteAccess"))
        self.assertTrue(result.get("hasReadAccess"))
        self.assertFalse(result.get("canPostOnReadonly"))

    def test_get_mail_thread_data_res_users(self):
        """Test flow get thread data for `res.users` record"""
        result = self.res_users_internal_user_email._get_mail_thread_data([])
        self.assertTrue(result.get("hasReadAccess"))
        self.assertFalse(result.get("hasWriteAccess"))

    def test_get_mail_thread_data_empty_user(self):
        """Test flow get thread data for `res.users` empty record"""
        result = self.env["res.users"]._get_mail_thread_data([])
        self.assertFalse(result.get("hasReadAccess"))
        self.assertFalse(result.get("hasWriteAccess"))
