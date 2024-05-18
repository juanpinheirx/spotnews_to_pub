from django.db import models
from utils.validators import (
    validate_date_format,
    validate_fields,
    validate_fields_with_200,
    validate_if_is_not_blank,
    validate_title_with_two_words,
)


class Category(models.Model):
    name = models.CharField(max_length=200, validators=[validate_fields])

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, validators=[validate_fields])
    email = models.EmailField(max_length=200, validators=[validate_fields])
    password = models.CharField(max_length=200, validators=[validate_fields])
    role = models.CharField(max_length=200, validators=[validate_fields])

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            validate_if_is_not_blank,
            validate_fields_with_200,
            validate_title_with_two_words,
        ],
    )
    content = models.TextField(validators=[validate_if_is_not_blank])
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news"
    )
    created_at = models.DateField(
        auto_now_add=True, validators=[validate_date_format]
    )
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(
        Category, related_name="news", validators=[validate_if_is_not_blank]
    )

    def __str__(self):
        return self.title
