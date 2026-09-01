from rest_framework.permissions import IsAuthenticated
from core.views import TenantScopedViewSet
from .models import ParentGuardian, Student
from .serializers import ParentGuardianSerializer, StudentSerializer

class ParentGuardianViewSet(TenantScopedViewSet):
    queryset = ParentGuardian.objects.all()
    serializer_class = ParentGuardianSerializer
    permission_classes = [IsAuthenticated]

class StudentViewSet(TenantScopedViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]