from django import forms
from django.contrib.auth import get_user_model

from schoolify.questions.models import Question, Answer


class QuestionForm(forms.ModelForm):
#TODO: kak da kaja che student = personal_number
    class Meta:
        model = Question
        # exclude = ('student',)
        fields = '__all__'
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'placeholder': 'Please type your question here...',
                })
        }





class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add your comment...',
                })
        }