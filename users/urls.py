"""Urls users"""
from django.urls import path
from users.views import HomePageView, LoginUserView, logout_users,\
    RegisterUserView

app_name = "users"


urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("register", RegisterUserView.as_view(), name="register"),
    path("login", LoginUserView.as_view(), name="register"),
    path("logout", logout_users, name="logout")
]
