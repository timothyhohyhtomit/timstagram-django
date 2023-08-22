from django.urls import path
from . import views

urlpatterns = [
    path("", views.story_index, name="story_index")
]