from django.contrib import admin
from schoolify.questions.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ordering = ('question',)
    list_display = ['question', 'related_school_subject']
    search_fields = ("question",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    ordering = ('comment_text',)
    list_display = ['comment_text', 'user']
    search_fields = ("comment_text",)
