from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'subject', 'qualification', 'is_active', 'joined_at', 'issuedate', 'valid_till')
    search_fields = ('name', 'email', 'mobile', 'aadhar', 'subject')
    list_filter = ('subject', 'is_active', 'joined_at', 'issuedate', 'valid_till')