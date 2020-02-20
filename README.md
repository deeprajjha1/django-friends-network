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
The User objects in Model is default django.contrib.auth.models User class and is a simple bean. Further in Model we have our own custom friendship class which has 2 fields from_friend and to_friend. Say

open shell : python manage.py shell
a) In order to create and push Users in DB just execute bulk_user_push.py :
    from friends import bulk_user_push (be careful of pwd)
 
b) In order to create friendship relationship just execute make_friends.py :
    from friends import make_friends.py (be careful of pwd). This will create a table called friends_friendship in database :
    
C:\PostgreSQL\11\bin>psql.exe -U djha -d testdb1
psql (11.5)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

testdb1=> select * from friends_friendship;
 id  | from_friend_id | to_friend_id
-----+----------------+--------------
   1 |              2 |            3
   2 |              2 |            4
   3 |              2 |            5
   4 |              2 |            6
   5 |              2 |            7
   6 |              2 |            8
   7 |              2 |            9
   

Now start the server : 
python manage.py runserver

A simple get query to http://localhost:8000/admin/auth/user/ will list users list in django dashboard
However our api exposed at friends with user id as param will return list of friends for that user as json


