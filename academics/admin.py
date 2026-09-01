from django.contrib import admin
from .models import AcademicYear, Term, GradeLevel, Stream, Subject

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'school', 'is_current', 'created_at')
    list_filter = ('school', 'is_current')
    search_fields = ('year', 'school__name')

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year', 'is_current', 'start_date', 'end_date')
    list_filter = ('is_current', 'academic_year__school')
    search_fields = ('name', 'academic_year__year')

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'school')
    list_filter = ('school',)
    search_fields = ('name', 'code', 'school__name')

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level')
    list_filter = ('grade_level__school', 'grade_level')
    search_fields = ('name', 'grade_level__name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'school', 'is_compulsory')
    list_filter = ('school', 'is_compulsory')
    search_fields = ('name', 'code', 'school__name')