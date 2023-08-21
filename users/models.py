from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class Member(AbstractUser):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    displayed_name = models.CharField(max_length=30)
    followers = models.ManyToManyField("self", blank=True)
    followings = models.ManyToManyField("self", black=True)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(default=datetime.utcnow, blank=True)
    avatar_url = models.URLField(null=True)
    is_activated = models.BooleanField(default=True)
