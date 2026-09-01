from rest_framework.permissions import IsAuthenticated
from core.views import TenantScopedViewSet
from .models import AcademicYear, Term, GradeLevel, Stream, Subject
from .serializers import (
    AcademicYearSerializer, TermSerializer, 
    GradeLevelSerializer, StreamSerializer, SubjectSerializer
)

class AcademicYearViewSet(TenantScopedViewSet):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated]

class TermViewSet(TenantScopedViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Term.objects.all()
        if user.is_superuser or user.role == 'SUPER_ADMIN':
            return queryset
        if hasattr(user, 'school') and user.school:
            return queryset.filter(academic_year__school=user.school)
        return queryset.none()

class GradeLevelViewSet(TenantScopedViewSet):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer
    permission_classes = [IsAuthenticated]

class StreamViewSet(TenantScopedViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Stream.objects.all()
        if user.is_superuser or user.role == 'SUPER_ADMIN':
            return queryset
        if hasattr(user, 'school') and user.school:
            return queryset.filter(grade_level__school=user.school)
        return queryset.none()

class SubjectViewSet(TenantScopedViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]