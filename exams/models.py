import uuid
from django.db import models
from core.models import School
from academics.models import AcademicYear, Term, GradeLevel, Subject
from students.models import Student

class Exam(models.Model):
    """
    Inafafanua mtihani husika, mfano: Mid-Term Exam, Terminal Exam, au Annual Exam.
    """
    class ExamType(models.TextChoices):
        MID_TERM = 'MID_TERM', 'Mid-Term'
        TERMINAL = 'TERMINAL', 'Terminal'
        ANNUAL = 'ANNUAL', 'Annual'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(max_length=150, help_text="Mfano: Mtihani wa Muhula wa Kwanza 2026")
    exam_type = models.CharField(max_length=20, choices=ExamType.choices)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='exams')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='exams')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, related_name='exams')
    is_published = models.BooleanField(default=False, help_text="Matokeo yakishachapishwa wazazi wanaweza kuyaona")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.grade_level.name}"


class ExamSubject(models.Model):
    """
    Inaunganisha mtihani na masomo yanayofanyiwa mtihani huo kwa darasa hilo.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exam_subjects')
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    def __str__(self):
        return f"{self.exam.name} -> {self.subject.name}"


class Mark(models.Model):
    """
    Inatunza alama alizopata mwanafunzi kwenye somo fulani kwenye mtihani maalum.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='marks')
    exam_subject = models.ForeignKey(ExamSubject, on_delete=models.CASCADE, related_name='marks')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5, blank=True, null=True, help_text="Mfano: A, B, C, D, F")
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('exam_subject', 'student')

    def __str__(self):
        return f"{self.student.first_name}: {self.marks_obtained} marks"