from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient_role', 'sent_at', 'is_read', 'read_at')
    search_fields = ('title', 'message')
    list_filter = ('recipient_role', 'is_read', 'sent_at')