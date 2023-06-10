from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView

from .models import Chat, ChatMembers, FriendRequest
from .permissions import FriendRequestPermission
from .serializers import FriendRequestSerializer


class ChatView(APIView):
    http_method_names = ['get']
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        chat_groups = Chat.objects.filter(request.user)


class FriendRequestViewSet(CreateModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = (IsAuthenticated, FriendRequestPermission)

    def filter_queryset(self, queryset):
        return queryset.filter(second_user=self.request.user, is_active=True)
