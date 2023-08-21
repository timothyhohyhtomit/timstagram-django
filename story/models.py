from django.db import models
from datetime import datetime, timedelta


class StoryManager(models.Manager):
    # get_expire_at returns the default expire datetime of a story, i.e. 24 hours after publish datetime
    def get_expire_at(self):
        return datetime.utcnow() + timedelta(days=1)

class Story(models.Model):
    id = models.IntegerField(primary_key=True)
    # if the owner of the story got removed, treat story as anonymous
    member_id = models.ForeignKey("Member", null=True, on_delete=models.SET_NULL)
    # publish datetime
    publish_at = models.DateTimeField(default=datetime.utcnow)
    # expire datetime
    expire_at = models.DateTimeField(default=StoryManager.objects.get_expire_at)

class StoryLike(models.Model):
    id = models.IntegerField(primary_key=True)
    # if the member who issued the like got removed, treat like as anonymous
    member_id = models.ForeignKey("Member", on_delete=models.SET_NULL)
    # if the story associated with the like was removed, remove the like as well
    story_id = models.ForeignKey("Story", on_delete=models.CASCADE)
