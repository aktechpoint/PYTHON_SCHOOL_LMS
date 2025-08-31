from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message_type', 'sent_at', 'is_read', 'read_at', 'is_deleted')
    search_fields = ('sender', 'receiver', 'text')
    list_filter = ('message_type', 'is_read', 'is_deleted', 'sent_at')