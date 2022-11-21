from rest_framework import permissions


class IsModeratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.is_superuser:
            return True
        return (request.method in permissions.SAFE_METHODS
                or request.user.role in ['admin', 'moderator'])


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin
