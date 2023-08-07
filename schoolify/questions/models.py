from django.contrib.auth import get_user_model
from django.db import models
from schoolify.auth_app.models import Profile

UserModel = get_user_model()


class Question(models.Model):
    MAX_SCHOOL_SUBJECT_LEN = 11
    MATHEMATICS = 'Mathematics'
    ENGLISH = 'English'
    MUSIC = 'Music'
    COOKING = 'Cooking'

    TYPES_OF_SUBJECTS = (
        (MATHEMATICS, MATHEMATICS),
        (ENGLISH, ENGLISH),
        (MUSIC, MUSIC),
        (COOKING, COOKING)
    )
    related_school_subject = models.CharField(
        max_length=MAX_SCHOOL_SUBJECT_LEN,
        choices=TYPES_OF_SUBJECTS,
        null=False,
        blank=False,
    )
    question = models.TextField(
        null=False,
        blank=False,
    )
    created_on = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )
    student = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'Student with ID :{self.student} asked question for {self.related_school_subject} on {self.created_on}.'


class Answer(models.Model):
    MAX_ANSWER_LEN = 300
    comment_text = models.TextField(
        max_length=MAX_ANSWER_LEN,
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    to_question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'User with ID: {self.user} gave a reply to question: "{self.to_question}"'




