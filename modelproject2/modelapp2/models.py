from django.db import models


class Fruits(models.Model):
    fno=models.IntegerField()
    fname=models.CharField(max_length=25)
    fprice=models.FloatField()
    fseller=models.CharField(max_length=25)
    fcate=models.CharField(max_length=20)
