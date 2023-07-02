from unittest import TestCase
from main import User_login
from notification import User_notification


class Test_User_login(TestCase):
    def test_connectedDatabase(self):
        self.assertEqual(len(User_login.link) == 0, False)
    def test_username(self):
        self.assertEqual(len(User_login.username) == 0, False)
    def test_password(self):
        self.assertEqual(len(User_login.password) == 0, False)

class Test_User_notification(TestCase):
    def test_connectedDatabase(self):
        self.assertEqual(len(User_login.link) == 0, False)
    def test_name(self):
        self.assertEqual(len(User_notification.name) == 0, False)
    def test_lastname(self):
        self.assertEqual(len(User_notification.lastname) == 0, False)
    def test_studentNumber(self):
        self.assertEqual(len(User_notification.studentNumber) == 11, True)
    def test_trIdentification(self):
        self.assertEqual(len(User_notification.trIdentification) == 11, True)
