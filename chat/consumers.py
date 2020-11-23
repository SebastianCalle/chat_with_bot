"""chat/consumers.py"""

# Utils
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.utils import get_last_fifteen_messages

# Django
from django.contrib.auth import get_user_model
from django.http import Http404

# Models
from chat.models import Message


User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    """
        ChatConsumer handle the connection with the WebSocket
        throught the routing.
    """

    def connect(self):
        """This method handle the connection wiht the WebSocket."""

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """Leave room group."""
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def pull_messages(self):
        """Return the last messages."""
        print("PULL MESSAGES")
        messages = get_last_fifteen_messages()
        context = {
            'command': 'messages',
            'messages': [
                {
                    'author': message.author.username,
                    'content': message.content,
                    'created': str(message.created)
                } for message in messages
            ]
        }
        return self.send_chat_message(context)

    def new_message(self, data):
        """Storage new message."""
        author = data['from']
        user = User.objects.filter(username=author).first()
        if not user:
            raise Http404("Author does not exist")
        print('receive', data['message'])
        message = Message.objects.create(content=data['message'], author=user)
        contex = {
            'command': 'new_message',
            'message': {
                'author': message.author.username,
                'content': message.content,
                'created': str(message.created)
            }
        }
        return self.send_chat_message(contex)

    #command = {
    #    'pull_message': pull_message,
    #    'new_message': new_message
    #}

    def receive(self, text_data):
        """Receive message from WebSocket."""
        data = json.loads(text_data)
        if data['command'] == 'pull_messages':
            self.pull_messages()
        if data['command'] == 'new_message':
            self.new_message(data)
        #self.command[data['command']](self, data)

    def send_chat_message(self, message):
        """Send the message to chat_message."""
        print('message', message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        """Send the message to WebSocket."""
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        """Receive message from room group."""
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
