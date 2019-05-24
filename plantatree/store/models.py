from django.db import models


# Create your models here.


class Tree(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    soil = models.CharField(max_length=1)
    sun = models.CharField(max_length=1)
    food = models.CharField(max_length=1)
    water = models.CharField(max_length=1)
    pruning = models.CharField(max_length=1)
    max_height = models.IntegerField(default=-1)
    growth_rate = models.CharField(max_length=1)
    price = models.IntegerField(default=-1)

    def price_int(self):
        return self.price / 100

    def price_str(self):
        return f'{format(self.price / 100, ",.2f")}'

    def __str__(self):
        return f'{self.name}, {self.price_str()}'
