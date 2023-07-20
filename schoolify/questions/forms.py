from django import forms

from schoolify.questions.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('related_school_subject', 'question')
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'placeholder': 'Please type your question here...',
                })
        }

# TODO: check below
#         def save(self, commit=True):
#             question = super().save(commit=commit)
#             question = self.cleaned_data['question']
#             related_school_subject = self.cleaned_data['related_school_subject ']
#             question = Question(
#                 question=question,
#                 related_school_subject =related_school_subject ,
#                 student_id=student.pk,
#             )
#             if commit:
#                 question.save()
#             return question


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