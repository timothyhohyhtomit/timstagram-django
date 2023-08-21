from django.db import models

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    # if the owner of the post no longer exists, treat post as anonymous
    member_id = models.ForeignKey("Member", null=True, on_delete=models.SET_NULL)
    # number of images associated to this post
    n_img = models.IntegerField(default=1)
    # caption
    caption = models.TextField(null=False, blank=False)
    # number of likes
    n_like = models.IntegerField(default=0)

class PostImage(models.Model):
    id = models.IntegerField(primary_key=True)
    # if the member who uploaded the image no longer exists, treat image as anonymous
    member_id = models.ForeignKey("Member", on_delete=models.CASCADE)
    url = models.URLField(null=False)
    # if a post has mutiple images, this specifies the order in which the images are presented
    # if a post only has one image, set this to null
    order = models.IntegerField(null=True)

class PostLike(models.Model):
    id = models.IntegerField(primary_key=True)
    # if the member who issued the like no longer exists, remove the like
    member_id = models.ForeignKey("Member", on_delete=models.CASCADE)
    # if the post associated with the like was removed, remove the like as well
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)

class PostComment(models.Model):
    id = models.IntegerField(primary_key=True)
    # if the member who made the comment no longer exists, remove the comment
    member_id = models.ForeignKey("Member", on_delete=models.CASCADE)
    # if the post associated with the comment was removed, remove the comment as well
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    # content of comment
    comment = models.TextField(null=False, black=False)
