from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField(max_length=300)
    ammount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    weight = models.CharField(max_length=255)
    
