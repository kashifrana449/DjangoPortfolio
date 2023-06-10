from django.contrib import admin

from .models import FriendRequest, Friends, Chat, ChatMembers

# Register your models here.
admin.site.register(FriendRequest)
admin.site.register(Friends)
admin.site.register(Chat)
admin.site.register(ChatMembers)
