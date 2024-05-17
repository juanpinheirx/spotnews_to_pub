from django.db import models
from utils.validators import validate_name


class Category(models.Model):
    name = models.CharField(max_length=200, validators=[validate_name])

    def __str__(self):
        return self.name
