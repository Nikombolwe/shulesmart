import uuid
from django.db import models
from core.models import School
from academics.models import AcademicYear, GradeLevel
from students.models import Student

class FeeStructure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='fee_structures')
    name = models.CharField(max_length=100, help_text="Mfano: Ada ya Shule, Chakula, Transport")
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='fee_structures')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, related_name='fee_structures')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.grade_level.name} ({self.amount})"


class Invoice(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PARTIAL = 'PARTIAL', 'Partially Paid'
        PAID = 'PAID', 'Paid'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='invoices')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='invoices')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='invoices')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def balance(self):
        return self.total_amount - self.paid_amount

    def __str__(self):
        return f"Invoice {self.student.first_name} - {self.total_amount}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
        ('MOBILE_MONEY', 'Mobile Money (M-Pesa/Airtel/Tigo)'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='payments')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='CASH')
    reference_number = models.CharField(max_length=100, blank=True, null=True, help_text="Namba ya Muamala/Risiti")
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.amount_paid} for {self.invoice.student.first_name}"