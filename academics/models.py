import uuid
from django.db import models
from core.models import School

class AcademicYear(models.Model):
    """
    Mwaka wa Masomo (Mfano: 2026).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='academic_years')
    year = models.IntegerField(help_text="Mfano: 2026")
    is_current = models.BooleanField(default=False, help_text="Inaonyesha kama huu ndio mwaka unaoendelea")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year']
        unique_together = ['school', 'year']

    def __str__(self):
        return f"{self.year} - {self.school.name}"


class Term(models.Model):
    """
    Muhula wa Masomo (Mfano: Term 1, Term 2).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='terms')
    name = models.CharField(max_length=50, help_text="Mfano: Term 1 au Muhula wa Kwanza")
    is_current = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.academic_year.year})"


class GradeLevel(models.Model):
    """
    Ngazi ya Darasa (Mfano: Form 1, Form 2, Primary 1, Baby Class).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='grade_levels')
    name = models.CharField(max_length=100, help_text="Mfano: Form One / Darasa la Kwanza")
    code = models.CharField(max_length=20, help_text="Mfano: F1, STD1")

    class Meta:
        ordering = ['code']
        unique_together = ['school', 'code']

    def __str__(self):
        return f"{self.name} - {self.school.name}"


class Stream(models.Model):
    """
    Mkondo wa Darasa (Mfano: Stream A, Science Stream, Blue Stream).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, related_name='streams')
    name = models.CharField(max_length=50, help_text="Mfano: A, B, North, Gold")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.grade_level.name} {self.name}"


class Subject(models.Model):
    """
    Somo (Mfano: Basic Mathematics, English Language, Physics).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100, help_text="Mfano: Basic Mathematics")
    code = models.CharField(max_length=20, help_text="Mfano: MATH-01")
    is_compulsory = models.BooleanField(default=True, help_text="Kama ni somo la lazima au la hiyari")

    class Meta:
        ordering = ['name']
        unique_together = ['school', 'code']

    def __str__(self):
        return f"{self.name} ({self.code})"