from django import forms
from schoolify.questions.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('student',)
        # fields = '__all__'
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
            'answer_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add your answer...',
                })
        }

