from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom Login Endpoint inayotumia Custom Serializer yetu.
    """
    serializer_class = CustomTokenObtainPairSerializer


class TenantScopedViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet inayochuja data kulingana na shule ya mtumiaji aliye-login.
    Super Admin anaona data zote.
    """
    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        # Kama ni Super Admin, mruhusu aone data zote
        if user.is_superuser or user.role == 'SUPER_ADMIN':
            return queryset

        # Kama mtumiaji ana shule, mchuje aone za shule yake tu
        if hasattr(user, 'school') and user.school:
            return queryset.filter(school=user.school)

        # Kama hana shule na sio super admin, asipate kitu
        return queryset.none()