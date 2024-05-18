from django.core.exceptions import ValidationError


def validate_fields(value):
    if len(value) == 0:
        raise ValidationError("Este campo não pode estar vazio.")
    elif len(value) > 200:
        raise ValidationError(
            f"Certifique-se de que o valor tenha no máximo 200 caracteres (ele possui {len(value)})."  # noqa
        )


def validate_title_with_two_words(value):
    if len(value.split()) == 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_if_is_not_blank(value):
    if value == "":
        raise ValidationError(
            f"Certifique-se de que o valor tenha no máximo 200 caracteres (ele possui {len(value)})."  # noqa
        )


def validate_fields_with_200(value):
    if len(value) > 200:
        raise ValidationError(
            f"Certifique-se de que o valor tenha no máximo 200 caracteres (ele possui {len(value)})."  # noqa
        )


def validate_date_format(value):
    if not value.strftime("%Y-%m-%d"):
        raise ValidationError(
            f"O valor {value} tem um formato de data inválido. Deve ser no formato  YYYY-MM-DD."  # noqa
        )
