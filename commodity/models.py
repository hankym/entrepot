from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(u"商品",max_length=256)

    num  = models.IntegerField(u"库存")

    sale = models.IntegerField(u"已售")



    def my_property(self):

        return self.num - self.sale

    my_property.short_description = "剩余"
    remain = property(my_property)

    #img  = models.ImageField(upload_to='img')


    def __str__(self):

        return self.name

