from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'aadhar', 'role', 'is_active', 'created_at', 'issuedate', 'valid_till')
    search_fields = ('name', 'email', 'mobile', 'aadhar')
    list_filter = ('role', 'is_active', 'created_at', 'issuedate', 'valid_till')