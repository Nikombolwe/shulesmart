from django.contrib import admin
from .models import ParentGuardian, Student

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