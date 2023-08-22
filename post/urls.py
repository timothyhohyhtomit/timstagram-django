from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_index, name="post_index"),
    path("<int:post_id>/", views.post, name="post")
]
