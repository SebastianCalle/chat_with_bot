"""Chat Models"""

# Django
from django.db import models
from django.contrib.auth import get_user_model

# Third party imports
from model_utils.models import TimeStampedModel, SoftDeletableModel

User = get_user_model()


class Message(TimeStampedModel, SoftDeletableModel, models.Model, ):
    """Messages Model."""
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.CASCADE
    )
    content = models.TextField()

    def __str__(self):
        """String representation."""
        return f'{self.author}'

