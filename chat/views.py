"""View for Chat app."""
# Django
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    """Index view."""
    return render(request, 'chat/index.html')


@login_required(login_url='/users/login')
def room(request, room_name):
    """Room view."""
    return render(request, 'chat/room.html', {
        'room_name': mark_safe(json.dumps(room_name)),
        'username':  mark_safe(json.dumps(request.user.username))
    })
