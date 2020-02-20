from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from friends.serializers import FriendSerializer
from friends.models import *
# Create your views here.

@api_view(['GET','POST'])
def friend_list(request,id) :

    usr = User.objects.get(id=id)

    if request.method == 'GET' :
        # friends = usr.to_friend_set.all()

        friends = [friendship for friendship in usr.from_friend_set.all()]
        serializer = FriendSerializer(friends,many=True)
        return Response(serializer.data)

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def friend_list_level(request,userId,level) :

    usr = User.objects.get(id=userId)
    if request.method == 'GET' :
        # friends = usr.to_friend_set.all()

        friends = [friendship for friendship in usr.from_friend_set.all()]
        level -= 1
        while level > 0:
            nthLevelFriends =

        serializer = FriendSerializer(friends,many=True)
        return Response(serializer.data)

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


