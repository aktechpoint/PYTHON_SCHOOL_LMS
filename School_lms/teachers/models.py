from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    image = models.ImageField(upload_to='teachers/images/', blank=True, null=True)
    qualification = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issuedate = models.DateField(null=True, blank=True)
    valid_till = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.subject})"