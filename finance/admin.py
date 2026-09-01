from django.contrib import admin
from .models import FeeStructure, Invoice, Payment

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'academic_year', 'amount', 'school')
    list_filter = ('grade_level', 'academic_year', 'school')
    search_fields = ('name', 'school__name')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('student', 'academic_year', 'total_amount', 'paid_amount', 'status', 'school')
    list_filter = ('status', 'academic_year', 'school')
    search_fields = ('student__first_name', 'student__last_name', 'student__admission_number')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount_paid', 'payment_method', 'reference_number', 'payment_date', 'school')
    list_filter = ('payment_method', 'payment_date', 'school')
    search_fields = ('reference_number', 'invoice__student__first_name', 'invoice__student__last_name')