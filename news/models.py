from django.db import models
from utils.validators import validate_name


class Category(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])

    def __str__(self):
        return self.name
