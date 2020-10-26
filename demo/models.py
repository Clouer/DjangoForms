from django.db import models


class Book(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pass_id = models.CharField(max_length=100)
    luggage_weight = models.FloatField()
