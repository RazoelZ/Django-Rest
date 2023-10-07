from django.db import models

# Create your models here.


class Cars(models.Model):
    carsId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    model = models.CharField(max_length=255)


def __str__(self):
    return self.name
