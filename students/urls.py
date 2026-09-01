from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ParentGuardianViewSet, 
    StudentViewSet, 
    EnrollmentViewSet, 
    AttendanceViewSet
)

router = DefaultRouter()
router.register('parents', ParentGuardianViewSet, basename='parent')
router.register('students', StudentViewSet, basename='student')
router.register('enrollments', EnrollmentViewSet, basename='enrollment')
router.register('attendances', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
]