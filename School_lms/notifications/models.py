from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    recipient_role = models.CharField(max_length=20, choices=[
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('staff_admin', 'Staff Admin'),
        ('all', 'All'),
    ], default='all')
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.recipient_role})"