from rest_framework import serializers
from .models import ParentGuardian, Student, Enrollment, Attendance

class ParentGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentGuardian
        fields = '__all__'
        read_only_fields = ['school']


class StudentSerializer(serializers.ModelSerializer):
    grade_level_name = serializers.ReadOnlyField(source='grade_level.name')
    stream_name = serializers.ReadOnlyField(source='stream.name')

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['school']


class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.first_name')
    grade_name = serializers.ReadOnlyField(source='grade_level.name')

    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['school']


class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.first_name')

    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['school', 'recorded_by']