from rest_framework.permissions import BasePermission


class FriendRequestPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.id == request.data['first_user']
        return True
