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
