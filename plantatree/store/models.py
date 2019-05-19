from django.db import models


# Create your models here.


class ItemDescription(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    price = models.IntegerField(default=-1)
    item_type = models.CharField(max_length=20)
    picture_url = models.CharField(max_length=50)

    def get_dollars(self):
        return self.price / 100

    def __str__(self):
        return '%s, $%.2f' % (self.name, self.price / 100)


class TreeItem(models.Model):
    height = models.IntegerField(default=-1)
    age = models.IntegerField(default=-1)
    item_info = models.ForeignKey(ItemDescription,
                                  on_delete=models.CASCADE)


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

    def price_str(self):
        return '$%s' % (format(self.price / 100, ',.2f'))

    def __str__(self):
        return '%s, $%.2f' % (self.name, self.price / 100)
