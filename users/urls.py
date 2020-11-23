"""Urls users"""
from django.urls import path
from users.views import LoginUserView, logout_users,\
    RegisterUserView

app_name = "users"


urlpatterns = [
    path("register", RegisterUserView.as_view(), name="register"),
    path("login", LoginUserView.as_view(), name="register"),
    path("logout", logout_users, name="logout")
]
