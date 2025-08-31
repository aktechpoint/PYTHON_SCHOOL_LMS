from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'code', 
        'teacher', 
        'duration_weeks', 
        'start_date', 
        'end_date', 
        'is_active'
    )
    search_fields = ('name', 'code', 'teacher')
    list_filter = ('is_active', 'start_date', 'end_date', 'teacher')
