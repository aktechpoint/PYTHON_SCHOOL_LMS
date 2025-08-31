

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/images/', blank=True, null=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"