from django.contrib import admin
from .models import ParentGuardian, Student, Enrollment, Attendance

@admin.register(ParentGuardian)
class ParentGuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'school', 'email')
    list_filter = ('school',)
    search_fields = ('first_name', 'last_name', 'phone_number', 'school__name')
    ordering = ('first_name', 'last_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_number', 'first_name', 'last_name', 'gender', 'grade_level', 'stream', 'school', 'status')
    list_filter = ('status', 'gender', 'school', 'grade_level')
    search_fields = ('admission_number', 'first_name', 'last_name', 'school__name')
    ordering = ('admission_number',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'grade_level', 'stream', 'academic_year', 'is_active', 'school')
    list_filter = ('is_active', 'grade_level', 'academic_year', 'school')
    search_fields = ('student__first_name', 'student__last_name', 'student__admission_number', 'school__name')
    ordering = ('-enrolled_at',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status', 'recorded_by', 'school')
    list_filter = ('status', 'date', 'school')
    search_fields = ('student__first_name', 'student__last_name', 'student__admission_number', 'school__name')
    ordering = ('-date',)