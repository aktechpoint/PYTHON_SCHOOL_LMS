from django.db import models

class Result(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='results')
    exam = models.ForeignKey('exams.Exam', on_delete=models.CASCADE, related_name='results')
    marks_obtained = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5)
    remarks = models.TextField(blank=True, null=True)
    result_date = models.DateField(auto_now_add=True)
    is_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.exam} ({self.grade})"