from django.db import models
from django.core.validators import MinValueValidator

from accounts.models import ProfileUser


class UnitType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Units(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    unit_name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500)
    long_description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    image_url = models.URLField()
    pdf_url = models.URLField(blank=True)
    type = models.ForeignKey(UnitType, on_delete=models.CASCADE, blank=True)                # blank=True

    # user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    # make = models.CharField(max_length=200)
    # model = models.CharField(max_length=200)
    # description = models.TextField()
    # price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    # image_url = models.URLField()
    # type = models.ForeignKey(UnitType, on_delete=models.CASCADE, blank=True)                # blank=True

    def __str__(self):
        return f"{self.user} has {self.model}"
