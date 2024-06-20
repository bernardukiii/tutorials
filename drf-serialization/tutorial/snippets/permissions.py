from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # custom permissions to only allow owners to edit but still user viewable if not owner
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user