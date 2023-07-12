from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    message = {'message': 'Invalid permissions'}

    def has_permission(self, request, view):
        return not request.user.is_anonymous

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False

        return request.user.id == obj.user.id
