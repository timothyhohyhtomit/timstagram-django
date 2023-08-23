from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.logout_request, name="logout")
]