from rest_framework import serializers
from friends.models import Friendship
from django.contrib.auth.models import User


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['from_friend','to_friend']
