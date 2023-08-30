from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Предоставляет право доступа если пользователь является создателем привычки"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
