from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Book(models.Model):
    MAX_BOOK_NAME_LEN = 50
    MAX_AUTHOR_NAME_LEN = 25
    MAX_DESCRIPTION_LEN = 1000
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
    name = models.TextField(
        max_length=MAX_BOOK_NAME_LEN,
        null=False,
        blank=False,
    )
    author = models.TextField(
        max_length=MAX_AUTHOR_NAME_LEN,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LEN,
        null=True,
        blank=True,
    )
    school_subject = models.CharField(
        max_length=MAX_SCHOOL_SUBJECT_LEN,
        choices=TYPES_OF_SUBJECTS,
        null=False,
        blank=False,
    )
    number_of_pages = models.IntegerField(
        null=True,
        blank=True,
    )
    available_from = models.DateField(
        null=False,
        blank=False,
    )
    cover_image = models.URLField(
        null=True,
        blank=True,
    )
    last_booked_by = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} is written by {self.author}'
