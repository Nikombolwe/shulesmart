from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import School, User

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'subdomain', 'registration_number', 'is_active', 'created_at')
    search_fields = ('name', 'subdomain', 'registration_number')
    list_filter = ('is_active',)
    ordering = ('name',)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'school', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number', 'school__name')
    list_filter = ('role', 'is_staff', 'is_active', 'school')
    
    # Ongeza ShuleSmart custom fields kwenye UI ya Admin
    fieldsets = BaseUserAdmin.fieldsets + (
        ('ShuleSmart Specific Info', {'fields': ('school', 'role', 'phone_number')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('ShuleSmart Specific Info', {'fields': ('school', 'role', 'phone_number')}),
    )