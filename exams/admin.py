from django.contrib import admin
from .models import Exam, ExamSubject, Mark

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_type', 'grade_level', 'academic_year', 'term', 'is_published', 'school')
    list_filter = ('exam_type', 'is_published', 'academic_year', 'school')
    search_fields = ('name', 'school__name')

@admin.register(ExamSubject)
class ExamSubjectAdmin(admin.ModelAdmin):
    list_display = ('exam', 'subject', 'max_marks')
    list_filter = ('exam__school', 'subject')

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam_subject', 'marks_obtained', 'grade', 'school')
    list_filter = ('school', 'exam_subject__exam')
    search_fields = ('student__first_name', 'student__last_name', 'student__admission_number')