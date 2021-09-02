from unittest import TestCase
from day9 import MessageUser


class TestMessageUser(TestCase):

    def test_add_user_method(self):
        testing_message_user = MessageUser()
        self.assertEqual(0, len(testing_message_user.get_users()))
        testing_message_user.add_user("chuong", 12)
        self.assertEqual(1, len(testing_message_user.get_users()))
    pass
