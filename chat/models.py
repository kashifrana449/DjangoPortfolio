from datetime import date, datetime

from django.contrib.auth import get_user_model
from django.db import models


class FriendRequest(models.Model):
    first_user = models.ForeignKey(get_user_model(), related_name='fr_first_user', on_delete=models.DO_NOTHING)
    second_user = models.ForeignKey(get_user_model(), related_name='fr_second_user', on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    is_accepted = models.BooleanField(default=False, blank=False, null=False)

    created_date_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = 'friend_request'


class Friends(models.Model):
    friend_request = models.ForeignKey(FriendRequest, related_name='friend_request', null=False, blank=False,
                                       on_delete=models.DO_NOTHING)
    first_user = models.ForeignKey(get_user_model(), related_name='f_first_user', null=False, blank=False,
                                   on_delete=models.DO_NOTHING)
    second_user = models.ForeignKey(get_user_model(), related_name='f_second_user', null=False, blank=False,
                                    on_delete=models.DO_NOTHING)

    created_date_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = 'friends'
        unique_together = ('first_user', 'second_user')


class Chat(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_date_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = 'chat'


class ChatMembers(models.Model):
    chat = models.ForeignKey(Chat, related_name='group', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(get_user_model(), related_name='user', on_delete=models.DO_NOTHING)

    created_date_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    modified_date_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        db_table = 'chat_members'
        unique_together = ('chat', 'user')
