from rest_framework.permissions import IsAuthenticated
from core.views import TenantScopedViewSet
from .models import Exam, ExamSubject, Mark
from .serializers import ExamSerializer, ExamSubjectSerializer, MarkSerializer

class ExamViewSet(TenantScopedViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)


class ExamSubjectViewSet(TenantScopedViewSet):
    queryset = ExamSubject.objects.all()
    serializer_class = ExamSubjectSerializer
    permission_classes = [IsAuthenticated]


class MarkViewSet(TenantScopedViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)