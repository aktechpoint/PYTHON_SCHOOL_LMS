from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks_obtained', 'total_marks', 'percentage', 'grade', 'is_passed', 'result_date')
    search_fields = ('student__name', 'exam__name', 'grade')
    list_filter = ('grade', 'is_passed', 'result_date', 'exam')