"""chat_project URL Configuration """

# Django
from django.contrib import admin
from django.conf.urls import include
from django.urls import path


# Views
from users.views import HomePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('users/', include('users.urls')),
    path("", HomePageView.as_view(), name="homepage"),
]
