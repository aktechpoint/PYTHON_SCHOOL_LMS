from django.contrib import admin
from .models import Admission

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'class_applied', 'section_applied', 'admission_date', 'status')
    search_fields = ('student_name', 'father_name', 'mother_name', 'email')
    list_filter = ('class_applied', 'section_applied', 'status')