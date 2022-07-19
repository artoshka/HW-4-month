from django.db import models


# Create your models here.
class Foods(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(default=0)
    price = models.FloatField(default=1)
    is_avalable = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=False)


class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)