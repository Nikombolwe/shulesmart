from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AcademicYearViewSet, TermViewSet, GradeLevelViewSet, 
    StreamViewSet, SubjectViewSet
)

router = DefaultRouter()
router.register('academic-years', AcademicYearViewSet)
router.register('terms', TermViewSet)
router.register('grade-levels', GradeLevelViewSet)
router.register('streams', StreamViewSet)
router.register('subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]