from django.core.exceptions import ValidationError
from django.core import exceptions


def validate_len_personal_number(value):
    len_username = list(str(value))
    if len(len_username) != 10:
        raise exceptions.ValidationError('The personal number should consist of 10digits.')


def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('Name should start with a capital letter.')


def validate_school_year_range(value):
    if value < 1 or value > 12:
        raise ValidationError('School grade should be between 1 and 12.')


def image_size_validator_10mb(image_object):
    max_size = 10 * 1024 * 1024

    if image_object.size > max_size:
        return ValidationError('Image size can not be larger than 10MB')

