import uuid
from django.db import models
from django.conf import settings
from core.models import School, User
from academics.models import AcademicYear, GradeLevel, Stream


class ParentGuardian(models.Model):
    """
    Taarifa za Mzazi au Mlezi.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='parents')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='parent_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"


class Student(models.Model):
    """
    Taarifa za Mwanafunzi.
    """
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        GRADUATED = 'GRADUATED', 'Graduated'
        TRANSFERRED = 'TRANSFERRED', 'Transferred'
        SUSPENDED = 'SUSPENDED', 'Suspended'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_profile')
    admission_number = models.CharField(max_length=50, help_text="Namba ya Usajili ya Mwanafunzi")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Academic Placement
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.PROTECT, related_name='students')
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    
    # Family link
    parent = models.ForeignKey(ParentGuardian, on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['school', 'admission_number']
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"


class Enrollment(models.Model):
    """
    Kusajili Mwanafunzi Darasani kwa Mwaka wa Masomo.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='enrollments')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, related_name='enrollments')
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True, blank=True, related_name='enrollments')
    is_active = models.BooleanField(default=True)
    enrolled_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'academic_year')
        ordering = ['-enrolled_at']

    def __str__(self):
        return f"{self.student} - {self.grade_level} ({self.academic_year})"


class Attendance(models.Model):
    """
    Mahudhurio ya Kila Siku ya Mwanafunzi.
    """
    class Status(models.TextChoices):
        PRESENT = 'PRESENT', 'Present'
        ABSENT = 'ABSENT', 'Absent'
        LATE = 'LATE', 'Late'
        EXCUSED = 'EXCUSED', 'Excused'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='attendances')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PRESENT)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='recorded_attendances')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"