from django.db import models

from schoolify.auth_app.validators import image_size_validator_10mb
from schoolify.utils.mixins import CreatedAndUpdatedInfoMixIn


class AssignmentBaseModel(CreatedAndUpdatedInfoMixIn):
    class Meta:
        abstract = True

    MAX_SCHOOL_SUBJECT_LEN = 20

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
    school_subject = models.CharField(
        max_length=MAX_SCHOOL_SUBJECT_LEN,
        choices=TYPES_OF_SUBJECTS,
        null=False,
        blank=False,
    )
    assignment_name = models.TextField(
        verbose_name='Name of assignment',
        help_text='Please fill in the name of your assignment as per homework.',
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.assignment_name} in {self.school_subject}'


class AssignmentEnglish(AssignmentBaseModel):
    essay = models.TextField(
        help_text='Please write your essay here.',
        null=False,
        blank=False,
    )
    external_resources_used = models.URLField(
        help_text='Please write the URL of the external resource used.',
        null=True,
        blank=True,
    )


class AssignmentMathematics(AssignmentBaseModel):
    solution = models.TextField(
        help_text='Please write the solution here',
        null=False,
        blank=False,
    )


class AssignmentMusic(AssignmentBaseModel):
    song = models.FileField(
        help_text='Please upload a record of your song here',
        upload_to='songs',
    )


class AssignmentCooking(AssignmentBaseModel):
    recipe_name = models.TextField(
        help_text='Please enter the name of your recipe.',
        null=False,
        blank=False,
    )
    dish_image = models.ImageField(
        upload_to='dishes',
        validators=(image_size_validator_10mb,),
        help_text='Please upload a picture of your dish.',
        null=True,
        blank=True,
    )
    ingredients = models.TextField(
        help_text='Please fill in the ingredients of your dish.',
        null=False,
        blank=False
    )
    preparation_time = models.TimeField(
        help_text='Please fill in the full reparation time, together with cooking time.',
        null=False,
        blank=False,
    )