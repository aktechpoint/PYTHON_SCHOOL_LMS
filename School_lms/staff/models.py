from django.db import models


class Staff(models.Model):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('staff_admin', 'Staff Admin'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)  # better to keep unique
    aadhar = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    image = models.ImageField(upload_to='staff/images/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issuedate = models.DateField(null=True, blank=True)
    valid_till = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.role.capitalize()}"
