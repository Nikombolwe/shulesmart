from django.contrib import admin
from .models import Announcement, Notification

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_audience', 'created_by', 'school', 'created_at')
    list_filter = ('target_audience', 'school')
    search_fields = ('title', 'message')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'title', 'is_read', 'school', 'created_at')
    list_filter = ('is_read', 'school')
    search_fields = ('title', 'recipient__email')