import unittest
from django.contrib.auth.models import User
from friends.serializers import UserSerializer


class UserTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_userCheck(self):
        usr = User.objects.get(id=23)
        self.assertEqual(usr.username ,'user22')
        self.assertIsNot(usr.username ,'user23')
