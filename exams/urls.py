from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExamViewSet, ExamSubjectViewSet, MarkViewSet

router = DefaultRouter()
router.register('exams', ExamViewSet, basename='exam')
router.register('exam-subjects', ExamSubjectViewSet, basename='exam-subject')
router.register('marks', MarkViewSet, basename='mark')

urlpatterns = [
    path('', include(router.urls)),
]