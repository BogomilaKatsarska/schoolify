from django import forms
from schoolify.questions.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('student',)
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'placeholder': 'Please type your question here...',
                })
        }


class QuestionEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].disabled = True

    class Meta:
        model = Question
        fields = '__all__'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add your answer...',
                }),
        }


class AnswerEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['to_question'].disabled = True

    class Meta:
        model = Answer
        fields = '__all__'
