from rest_framework import permissions

class IsSchoolAdminOrReadOnly(permissions.BasePermission):
    """
    Ruhusu School Admin na Super Admin kufanya mabadiliko yoyote (POST, PUT, DELETE).
    Watumiaji wengine (Teachers, Students, Parents) wana uwezo wa kusoma tu (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        # Mtu yeyote aliye-login anaruhusiwa kusoma (GET requests)
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Mabadiliko (POST, PUT, DELETE) yanaruhusiwa kwa Admins tu
        return (
            request.user and 
            request.user.is_authenticated and 
            (request.user.is_superuser or request.user.role in ['SUPER_ADMIN', 'SCHOOL_ADMIN'])
        )


class IsSuperAdmin(permissions.BasePermission):
    """
    Ruhusu Super Admin tu kufanya action husika.
    """
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            (request.user.is_superuser or request.user.role == 'SUPER_ADMIN')
        )