from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Friendship(models.Model):
  from_friend = models.ForeignKey(
    User, related_name='from_friend_set',
          on_delete=models.DO_NOTHING,
  )
  to_friend = models.ForeignKey(
    User, related_name='to_friend_set',
          on_delete=models.DO_NOTHING,
  )

  class Meta:
      unique_together = (('to_friend', 'from_friend'), )

"""
class Friends :
    title = models.CharField(max_length=100,blank=True,default='')
    friends = models.ManyToManyField(User)

-------------------------------------------------------------------------------------------------

class Person(AbstractBaseUser, PermissionsMixin):
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')


class Relationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_people')

"""
