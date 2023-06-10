from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FriendRequest, Friends, Chat, ChatMembers


@receiver(post_save, sender=FriendRequest)
def add_friend(sender, instance, **kwargs):
    if not Friends.objects.filter(friend_request=1).exists() and instance.is_accepted:
        friend = Friends(first_user=instance.first_user, second_user=instance.second_user, friend_request=instance)
        friend.save()


@receiver(post_save, sender=Friends)
def add_chat(sender, instance, **kwargs):
    chat = Chat()
    chat.save()
    chat_members = [ChatMembers(chat=chat.id, user=instance.first_user.id), ChatMembers(chat=chat.id, user=instance.second_user.id)]
    ChatMembers.objects.bulk_create(chat_members)
