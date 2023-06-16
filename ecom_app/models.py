from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    sub_category = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    published_date = models.DateField()
    image = models.ImageField(upload_to='ecom_app/images', default="")

    def __str__(self):
        return self.product_name
