from django.db import models

class ChatMessage(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('doc', 'Document'),
    ]
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES, default='text')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='chat/images/', blank=True, null=True)
    audio = models.FileField(upload_to='chat/audio/', blank=True, null=True)
    video = models.FileField(upload_to='chat/video/', blank=True, null=True)
    doc = models.FileField(upload_to='chat/docs/', blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} to {self.receiver} ({self.message_type}) at {self.sent_at}"