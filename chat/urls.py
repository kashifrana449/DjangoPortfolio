from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FriendRequestViewSet

router = DefaultRouter()

router.register('friend-request', FriendRequestViewSet, 'friend-request')

urlpatterns = [
    path('', include(router.urls))
]
