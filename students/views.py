from rest_framework.permissions import IsAuthenticated
from core.views import TenantScopedViewSet
from .models import ParentGuardian, Student, Enrollment, Attendance
from .serializers import (
    ParentGuardianSerializer, StudentSerializer, 
    EnrollmentSerializer, AttendanceSerializer
)

class ParentGuardianViewSet(TenantScopedViewSet):
    queryset = ParentGuardian.objects.all()
    serializer_class = ParentGuardianSerializer
    permission_classes = [IsAuthenticated]


class StudentViewSet(TenantScopedViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class EnrollmentViewSet(TenantScopedViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)


class AttendanceViewSet(TenantScopedViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Inahifadhi shule na mwalimu/admin aliyetengeneza ripoti ya mahudhurio kiutomatiki
        serializer.save(
            school=self.request.user.school,
            recorded_by=self.request.user
        )