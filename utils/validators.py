from django.core.exceptions import ValidationError


def validate_name(value):
    if len(value) == 0 or len(value) < 200:
        raise ValidationError("Name must be between 1 and 200 characters")
