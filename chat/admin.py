from django.contrib import admin

# Models.
from chat.models import Message, Room, Contact


admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(Room)
