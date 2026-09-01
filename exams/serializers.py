from rest_framework import serializers
from .models import Exam, ExamSubject, Mark

class ExamSubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subject.name')

    class Meta:
        model = ExamSubject
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    exam_subjects = ExamSubjectSerializer(many=True, read_only=True)
    grade_name = serializers.ReadOnlyField(source='grade_level.name')
    term_name = serializers.ReadOnlyField(source='term.name')

    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ['school']


class MarkSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.first_name')
    student_lastname = serializers.ReadOnlyField(source='student.last_name')

    class Meta:
        model = Mark
        fields = '__all__'
        read_only_fields = ['school']