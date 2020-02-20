# django-friends-network
Friend network created using django framework with postgres DB. 

This is a simple django rest based impl of Users having 2 way friendship and apis to view friend list of a particular user.

Setup :
1) Add python to System path variable
2) pip install django
3) pip install djangorestframework

Install Postgres DB server create a superuser and launch its pgbench and create a testdb to work with.
In order to interact with postgres from django setup psycopg2 :

4) pip install psycopg2
(Its a nightmare installing on windows because psycopg2 will need Visual VC++ package beyond 2016 release or so to work with Postgres)
Default sqllite is good and comes with easy view dbbrowser but it doesnt have supports for concurrent bulk requests

The project name is findfriends and app name is friend.
The User objects in Model is default django.contrib.auth.models User class and is a simple bean. Further in Model we have our own custom friendship class which has 2 fields of type User as from_friend and to_friend. Say

open shell : python manage.py shell
a) In order to create and push Users in DB just execute bulk_user_push.py :
    from friends import bulk_user_push (be careful of pwd)
 
b) In order to create friendship relationship just execute make_friends.py :
    from friends import make_friends.py (be careful of pwd). This will create a table called friends_friendship in database :

![alt text](https://github.com/deeprajjha1/media/blob/master/friendshipTable.png)   

Now start the server : 
python manage.py runserver

hit browser with http://localhost:8000/admin/auth/user/ will list users list in django dashboard
However our api exposed at friends with user id as param will return list of friends for that user as json:
http://localhost:8000/friends/2/ (Make_friends code created user3 to user100 friends of User2)

![alt text](https://github.com/deeprajjha1/media/blob/master/friends_user2.png)

