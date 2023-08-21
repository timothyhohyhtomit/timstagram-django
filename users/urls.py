from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_index, name="user_index"),
    path("<int:member_id>/", views.user_profile, name="user_profile")
]
