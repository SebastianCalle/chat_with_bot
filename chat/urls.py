"""Chat Urls"""

# Django
from django.urls import path, re_path

from chat.views import index, room

urlpatterns = [
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
