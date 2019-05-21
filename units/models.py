from django.db import models
from django.core.validators import MinValueValidator

from accounts.models import ProfileUser


class UnitType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Units(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    image_url = models.URLField()
    type = models.ForeignKey(UnitType, on_delete=models.CASCADE)                # blank=True

    def __str__(self):
        return f"{self.user} has {self.make}"
