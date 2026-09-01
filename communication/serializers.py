from rest_framework import serializers
from .models import Announcement, Notification

class AnnouncementSerializer(serializers.ModelSerializer):
    creator_name = serializers.ReadOnlyField(source='created_by.first_name')

    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ['school', 'created_by']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['school', 'is_read']