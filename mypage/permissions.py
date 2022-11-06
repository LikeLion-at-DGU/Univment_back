from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """게시물 작성자만 접근 가능하게 하기"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user == obj.user:
                return True
            return False
        else:
            return False