from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentGuardianViewSet, StudentViewSet

router = DefaultRouter()
router.register('parents', ParentGuardianViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]