from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsFinance(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role and request.user.role.name == 'Finance'

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role and request.user.role.name == 'Manager'

class IsWorker(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role and request.user.role.name == 'Worker' 