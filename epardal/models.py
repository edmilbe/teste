from django.db import models
# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    height = models.DecimalField(max_digits=6, decimal_places=2)