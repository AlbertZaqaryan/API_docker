from django.db import models

# Create your models here.

class Car(models.Model):

    name = models.CharField('Car name', max_length=60)
    price = models.PositiveIntegerField('Car price')
    year = models.PositiveIntegerField('Car year')

    def __str__(self):
        return self.name

class Phone(models.Model):

    name = models.CharField('Phone name', max_length=60)
    price = models.PositiveIntegerField('Phone price')

    def __str__(self):
        return self.name