from django.db import models

class Exam(models.Model):
    TEST_TYPE_CHOICES = [
        ('mcq', 'MCQ'),
        ('written', 'Written'),
        ('practical', 'Practical'),
    ]
    name = models.CharField(max_length=100)
    exam_code = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    exam_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()
    test_type = models.CharField(max_length=20, choices=TEST_TYPE_CHOICES, default='mcq')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.exam_code})"

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=255, blank=True, null=True)
    option_b = models.CharField(max_length=255, blank=True, null=True)
    option_c = models.CharField(max_length=255, blank=True, null=True)
    option_d = models.CharField(max_length=255, blank=True, null=True)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], blank=True, null=True)
    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Q: {self.text[:50]}..."