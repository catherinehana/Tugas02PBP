from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    picture = models.URLField(max_length=300)
    ammount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    weight = models.CharField(max_length=255)