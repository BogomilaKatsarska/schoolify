from django.core.exceptions import ValidationError


def image_size_validator_10mb(image_object):
    max_size = 10 * 1024 * 1024

    if image_object.size > max_size:
        return ValidationError('Image size can not be larger than 10MB')
