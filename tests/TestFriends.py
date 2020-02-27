import unittest
from friends.models import *


class FriendTest(unittest.TestCase):
    def setUp(self):
        pass

    # Remember we made user2 (idx=3) to user100 (idx=101) user1's friend
    def test_friendCheck(self):
        usr = User.objects.get(id=20) #Gets User19
        friends = usr.to_friend_set.get() #Gets the friendship object of user 19 friend which is user1 here
        self.assertEqual(friends.from_friend.username ,'user1')
        self.assertIsNot(friends.from_friend.username, 'user3')
