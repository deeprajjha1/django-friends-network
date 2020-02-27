from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from friends.serializers import UserSerializer,FriendSerializer
from friends.models import *

@api_view(['GET','POST'])
def user_list(request) :

    usrs = User.objects.all()
    serializer = None

    if request.method == 'GET' :
        serializer = UserSerializer(usrs,many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def user(request,id) :

    serializer = None
    usr = User.objects.get(id=id)

    if request.method == 'GET' :
        serializer = UserSerializer(usr,many=False)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def friend_list(request,id) :

    usr = User.objects.get(id=id)

    if request.method == 'GET' :
        # friends = usr.to_friend_set.all()

        friends = [friendship for friendship in usr.from_friend_set.all()]
        serializer = FriendSerializer(friends,many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



"""
@api_view(['GET'])
def friend_list_level(request,userId,level) :
    serializer = None
    usr = User.objects.get(id=userId)
    if request.method == 'GET' :

        friends = [friendship for friendship in usr.from_friend_set.all()]
        serializer = FriendSerializer(friends,many=True)
        return Response(serializer.data)

    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""
