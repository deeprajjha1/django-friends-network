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


def snippet_detail(request,pk):
    """
    Retrieve update or delete a code snippet
    """
    try:
        friend = Friendship.objects.get(pk=pk)
    except friendship.DoesNotExists:
        return HttpResponse(status=404)


    if request.method == 'GET' :
        serializer = FriendSerializer(friend)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT' :
        serializer = FriendSerializer(friend)



"""

def add_friend(request, username):
    if request.user.is_authenticated():
        user = Person.objects.get_by_natural_key(username)
        Relationship.objects.get_or_create(
            from_person=request.user,
            to_person=user)
        return HttpResponseRedirect('/profile/')



def show_friends(request, username):
    user = Person.objects.get_by_natural_key(username)
    rel = user.relationships.filter(
        to_people__from_person=user)
    args = {'friends': rel}
    return render(request, "profile/friend_list.html", args)

-------------------------------------------------------------------------------------------------------------------

class UserViewSet(viewsets.ModelViewSet) :

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet) :

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""
