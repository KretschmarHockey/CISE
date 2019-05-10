from django.db import models

# Create your models here.

class TreeItem(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    height = models.IntegerField(default=-1)
    age = models.IntegerField(default=-1)
    price = models.IntegerField(default=-1)
    picture_url = models.CharField(max_length=50)

    def get_dollars(self):
        return price / 100

    def __str__(self):
        return '%s, $%.2f' % (self.name, self.price / 100)