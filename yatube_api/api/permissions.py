from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    # Определяет права на уровне объекта
    def has_object_permission(self, request, view, obj):
        return True
