from django.db import models

class Admission(models.Model):
    student_name = models.CharField(max_length=100)
    dob = models.DateField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    previous_school = models.CharField(max_length=150, blank=True)
    admission_date = models.DateField(auto_now_add=True)
    class_applied = models.CharField(max_length=20)
    section_applied = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"{self.student_name} - {self.class_applied}"