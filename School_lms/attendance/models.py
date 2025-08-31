from django.db import models

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('leave', 'Leave')], default='present')
    remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.status}"