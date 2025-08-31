from django.contrib import admin
from .models import IDCard

@admin.register(IDCard)
class IDCardAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'roll_no', 'class_name', 'section', 'card_number', 'issue_date', 'valid_till')
    search_fields = ('student_name', 'roll_no', 'card_number')
    list_filter = ('class_name', 'section', 'issue_date', 'valid_till')