from django.db import models

# Create your models here.

class ItemDescription(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    price = models.IntegerField(default=-1)
    item_type = models.CharField(max_length=20)
    picture_url = models.CharField(max_length=50)

    def get_dollars(self):
        return price / 100

    def __str__(self):
        return '%s, $%.2f' % (self.name, self.price / 100)

class TreeItem(models.Model):
    height = models.IntegerField(default=-1)
    age = models.IntegerField(default=-1)
    item_info = models.ForeignKey(ItemDescription,
                on_delete=models.CASCADE)

