"""View for Chat app."""
# Django
from django.shortcuts import render

# Create your views here.


def index(request):
    """Index view."""
    return render(request, 'chat/index.html')


def room(request, room_name):
    """Room view."""
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
