from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .permissions import IsSchoolAdminOrReadOnly

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom Login Endpoint inayotumia Custom Serializer yetu.
    """
    serializer_class = CustomTokenObtainPairSerializer


class TenantScopedViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet inayochuja data kulingana na shule ya mtumiaji
    na kuweka ulinzi wa majukumu (Role-Based Permissions).
    """
    permission_classes = [IsSchoolAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        if not user.is_authenticated:
            return queryset.none()

        # Super Admin anaona data zote
        if user.is_superuser or user.role == 'SUPER_ADMIN':
            return queryset

        # Watumiaji wa shule wanaona za shule yao tu
        if hasattr(user, 'school') and user.school:
            return queryset.filter(school=user.school)

        return queryset.none()