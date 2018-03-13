from rest_framework.permissions import BasePermission

from .models import User


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', '') == User.ADMIN or request.user.is_superuser


class IsDesignerUser(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', '') in [User.DESIGNER, User.ADMIN] or request.user.is_superuser


class IsOrganizerUser(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', '') in [User.DESIGNER, User.ADMIN,
                                                     User.ORGANIZER] or request.user.is_superuser


class IsReviewerUser(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', '') in [User.DESIGNER, User.ADMIN, User.ORGANIZER,
                                                     User.REVIEWER] or request.user.is_superuser
