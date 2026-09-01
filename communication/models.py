import uuid
from django.db import models
from core.models import School, User

class Announcement(models.Model):
    """
    Matangazo ya jumla yanayotolewa na uongozi wa shule kwa walimu, wazazi, au wanafunzi.
    """
    class TargetAudience(models.TextChoices):
        ALL = 'ALL', 'Wote (All)'
        TEACHERS = 'TEACHERS', 'Walimu Tu'
        PARENTS = 'PARENTS', 'Wazazi Tu'
        STUDENTS = 'STUDENTS', 'Wanafunzi Tu'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=200)
    message = models.TextField()
    target_audience = models.CharField(max_length=20, choices=TargetAudience.choices, default=TargetAudience.ALL)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='announcements')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_target_audience_display()})"


class Notification(models.Model):
    """
    Arifa za moja kwa moja (In-app notifications) kwa mtumiaji fulani kwenye mfumo.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='notifications')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=150)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.recipient.email} - {self.title}"