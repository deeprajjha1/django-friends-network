from friends.models import *
from django.contrib.auth.models import User

user1 = User.objects.get(id=2)
user2 = User.objects.get(id=3)

def make_friends(usr,start,n_records):

        for i in range(start, n_records):
            useri = User.objects.get(id=i)
            friendship = Friendship(from_friend=usr, to_friend=useri)
            friendship.save()

"""
make user2 (idx=3) to user100 (idx=101) user1 friend
and then
make user101 (idx=102) to user200 (idx=201) user2 friend
Hence 2nd level friends for user 1 would be immediate friends of user2
"""

make_friends(user1,3,101)
make_friends(user2,102,200)
