"""Chat utils"""

# Models
from chat.models import Message


def get_last_fifteen_messages():
    """Return the las fifteen messages."""
    return Message.objects.all().order_by('created')[:50]
