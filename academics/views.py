from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import AcademicYear, Term, GradeLevel, Stream, Subject
from .serializers import (
    AcademicYearSerializer, TermSerializer, 
    GradeLevelSerializer, StreamSerializer, SubjectSerializer
)

class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated]

class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated]

class GradeLevelViewSet(viewsets.ModelViewSet):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer
    permission_classes = [IsAuthenticated]

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]