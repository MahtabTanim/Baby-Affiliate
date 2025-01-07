from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100,null=False,default='')
    price = models.FloatField(null=False , default=0.8)
    description = models.TextField()
    image = models.URLField(null= False)
    affiliate_link = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
