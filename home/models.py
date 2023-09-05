from django.db import models


# Create your models here.

class ProductType(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    desc = models.CharField( max_length=5000)
    sub_desc = models.CharField( max_length=5000, default=True)
    image= models.ImageField( upload_to='home/images', height_field=None, width_field=None, max_length=None)
        
    def __str__(self):
        return self.product_name
    
class Inquiry(models.Model):
    inquiry_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    query = models.CharField(max_length=1000)

    def __str__(self):
        return self.full_name
    

class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(default="0123456789")
    description = models.CharField( max_length=500,null="true")

    def __str__(self):
        return self.email
    

class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.ImageField(upload_to='home/images', height_field=None, width_field=None, max_length=None)
    price = models.IntegerField()
    description = models.CharField(max_length=5000)      
    sub_description = models.CharField(max_length=500)      
    name = models.CharField( max_length=50)
    quantity = models.IntegerField(default="0")
    type = models.CharField(max_length=250, null=True)
    company = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name