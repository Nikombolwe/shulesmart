from rest_framework import serializers
from .models import FeeStructure, Invoice, Payment

class FeeStructureSerializer(serializers.ModelSerializer):
    grade_name = serializers.ReadOnlyField(source='grade_level.name')
    year_name = serializers.ReadOnlyField(source='academic_year.name')

    class Meta:
        model = FeeStructure
        fields = '__all__'
        read_only_fields = ['school']


class InvoiceSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.first_name')
    balance = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['school', 'paid_amount', 'status']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['school']