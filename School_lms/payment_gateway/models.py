from django.db import models

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='payments')
    payer_name = models.CharField(max_length=100)
    payer_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=50, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=30, choices=[
        ('upi', 'UPI'),
        ('card', 'Card'),
        ('netbanking', 'Net Banking'),
        ('cash', 'Cash'),
        ('other', 'Other'),
    ], default='upi')

    def __str__(self):
        return f"{self.payer_name} - {self.amount} ({self.status})"