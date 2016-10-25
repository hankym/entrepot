from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(u"商品",max_length=256)

    num  = models.IntegerField(u"库存")

    img  = models.ImageField(upload_to='img')


    def __str__(self):

        return self.name

