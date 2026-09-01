from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ParentGuardian, Student
from .serializers import ParentGuardianSerializer, StudentSerializer

class ParentGuardianViewSet(viewsets.ModelViewSet):
    queryset = ParentGuardian.objects.all()
    serializer_class = ParentGuardianSerializer
    permission_classes = [IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]