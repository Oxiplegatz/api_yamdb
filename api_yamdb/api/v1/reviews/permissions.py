from rest_framework import permissions


class IsModeratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.is_superuser:
            return True
        return (request.method in permissions.SAFE_METHODS
                or request.user.role in ['admin', 'moderator'])
