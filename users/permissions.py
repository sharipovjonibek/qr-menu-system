from rest_framework.permissions import BasePermission

class IsWaiter(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=="waiter"

class IsCashier(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=="cashier"

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=="admin"