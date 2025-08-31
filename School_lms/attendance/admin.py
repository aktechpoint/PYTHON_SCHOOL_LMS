from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'roll_no', 'date', 'status', 'remarks')
    search_fields = ('student_name', 'roll_no')
    list_filter = ('status', 'date')