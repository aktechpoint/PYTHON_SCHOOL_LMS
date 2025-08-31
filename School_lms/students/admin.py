
# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'student_class', 'section', 'father_name', 'mother_name', 'mobile', 'email', 'created_at')
    search_fields = ('name', 'roll_no', 'email', 'father_name', 'mother_name')
    list_filter = ('student_class', 'section', 'created_at')