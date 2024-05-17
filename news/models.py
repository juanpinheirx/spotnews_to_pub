from django.db import models
from utils.validators import validate_fields


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
