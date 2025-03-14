from rest_framework.permissions import BasePermission


class IsBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        authors_names = obj.author.values_list('name', flat=True)

        return request.user.username in authors_names

