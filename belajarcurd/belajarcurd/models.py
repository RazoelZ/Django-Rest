from django.db import models


class Hero (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    mana = models.IntegerField()
    job = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.name
