from django.contrib import admin
from .models import Exam, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_code', 'course', 'exam_date', 'duration_minutes', 'total_marks', 'passing_marks', 'test_type', 'is_active')
    search_fields = ('name', 'exam_code', 'course')
    list_filter = ('course', 'exam_date', 'test_type', 'is_active')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'marks')
    search_fields = ('text',)