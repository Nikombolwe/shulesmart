import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    """
    Core Tenant Model: Kila shule kwenye SaaS yetu itakuwa na record hapa.
    Data zote za mfumo zitahusishwa na shule kupitia school_id kwa ajili ya Tenant Isolation.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="Jina la Shule (Mfano: St. Mary's Primary School)")
    registration_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    subdomain = models.SlugField(unique=True, help_text="Mfano: 'stmarys' kwa stmarys.shulesmart.com")
    is_active = models.BooleanField(default=True, help_text="Status ya shule iwapo inaruhusiwa kutumia mfumo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Custom User Model inayotumia Roles mbalimbali na kuunganishwa na Shule yake.
    """
    class Role(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
        SCHOOL_ADMIN = 'SCHOOL_ADMIN', 'School Owner/Admin'
        HEADMASTER = 'HEADMASTER', 'Headmaster/Principal'
        ACADEMIC_MASTER = 'ACADEMIC_MASTER', 'Academic Master'
        TEACHER = 'TEACHER', 'Teacher'
        PARENT = 'PARENT', 'Parent/Guardian'
        STUDENT = 'STUDENT', 'Student'
        ACCOUNTANT = 'ACCOUNTANT', 'Accountant'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(
        School, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='users',
        help_text="Shule anayotoka mtumiaji huyu. Inabaki tupu kwa Super Admin tu."
    )
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.TEACHER)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        school_name = self.school.name if self.school else "Global/Platform"
        return f"{self.username} - {self.get_role_display()} ({school_name})"