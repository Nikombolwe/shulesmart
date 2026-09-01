from rest_framework import serializers
from .models import ParentGuardian, Student

class ParentGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentGuardian
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    grade_level_name = serializers.ReadOnlyField(source='grade_level.name')
    stream_name = serializers.ReadOnlyField(source='stream.name')

    class Meta:
        model = Student
        fields = '__all__'