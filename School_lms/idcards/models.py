from django.db import models

class IDCard(models.Model):
    student_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    dob = models.DateField()
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to='idcards/images/', blank=True, null=True)
    issue_date = models.DateField(auto_now_add=True)
    valid_till = models.DateField()
    card_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"IDCard: {self.student_name} ({self.card_number})"