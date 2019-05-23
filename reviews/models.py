from django.db import models

from accounts.models import ProfileUser
from units.models import Units


class Review(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField()
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
