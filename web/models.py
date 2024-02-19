from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    price=models.FloatField()
    price2=models.FloatField()
    image=models.ImageField(upload_to='media')
    description = models.TextField()
    

# Create your models here.
    def __str__(self):
        return self.name
    


class slider(models.Model):
    name1=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    price1=models.FloatField()
    price2=models.FloatField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name1



class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name
    



class Electronics(models.Model):
    name=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    price=models.FloatField()
    price2=models.FloatField()
    image=models.ImageField(upload_to='media')
    description = models.TextField()

    def __str__(self):
        return self.name
    




class Baner(models.Model):
    name=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    price=models.FloatField()
    price2=models.FloatField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    
    


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Street_address=models.CharField(max_length=50)
    Town_city=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Zip=models.CharField(max_length=50)
    Number=models.IntegerField()
    email=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.First_name
    


class Order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/order_image')
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.IntegerField()
    paid=models.BooleanField(default=False)




    