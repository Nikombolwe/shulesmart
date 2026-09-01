from rest_framework.permissions import IsAuthenticated
from core.views import TenantScopedViewSet
from .models import Announcement, Notification
from .serializers import AnnouncementSerializer, NotificationSerializer

class AnnouncementViewSet(TenantScopedViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school, created_by=self.request.user)


class NotificationViewSet(TenantScopedViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Mtumiaji anaona arifa zake tu
        user = self.request.user
        if user.is_superuser or user.role == 'SUPER_ADMIN':
            return super().get_queryset()
        return super().get_queryset().filter(recipient=user)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)