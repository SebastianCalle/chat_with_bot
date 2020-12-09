"""Chat Models"""

# Django
from django.db import models
from django.contrib.auth import get_user_model

# Third party imports
from model_utils.models import TimeStampedModel, SoftDeletableModel

User = get_user_model()


class Contact(models.Model):
    """Contact model."""
    user = models.ForeignKey(
        User,
        related_name='frieds',
        on_delete=models.CASCADE
    )
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        """String representation."""
        return f"{self.user.username}"


class Message(TimeStampedModel, SoftDeletableModel, models.Model, ):
    """Messages Model."""
    contact = models.ForeignKey(
        Contact,
        related_name='messages',
        on_delete=models.CASCADE
    )
    content = models.TextField()

    def __str__(self):
        """String representation."""
        return f'{self.contact.user.username}'


class Room(TimeStampedModel, SoftDeletableModel, models.Model, ):
    """Room Model."""
    messages = models.ManyToManyField(
        Message,
        blank=True
    )
    participants = models.ManyToManyField(
        Contact,
        related_name='rooms',
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        """String representation."""
        return f"{self.name}"

    def get_last_fifteen_messages(self):
        """Return the las fifteen messages."""
        return self.messages.order_by('created')[:50]
