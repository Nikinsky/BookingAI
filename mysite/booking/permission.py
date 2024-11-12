from rest_framework import permissions


class ReviewUpdate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_name == request.user


class RoomOwnerCheck(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.hotel.owner == request.user


class BookingCheckPerson(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user_booking == request.user:
            return True
        return False


class CheckImg(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckCRUD(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'


class CheckOwnerObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'свободен':
            return True
        return False

class CheckBook(permissions.BasePermission):
    def has_permission(self, request, view):
        if  request.user.user_role == 'ownerUser':
            return False
        return True
