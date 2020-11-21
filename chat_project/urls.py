"""chat_project URL Configuration """

# Django
from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
]