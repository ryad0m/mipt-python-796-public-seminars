from django.contrib import admin

from app.models import Question, Answers

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass