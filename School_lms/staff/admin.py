from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'mobile', 'role', 
        'is_active', 'issuedate', 'valid_till', 'created_at'
    )
    search_fields = ('name', 'email', 'mobile', 'aadhar')
    list_filter = ('role', 'is_active', 'issuedate', 'valid_till')
    ordering = ('-created_at',)  # newest first
    readonly_fields = ('created_at', 'updated_at')  # prevents accidental edits
