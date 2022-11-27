
from django.db import models

# Create your models here.
class Userdetails(models.Model):
    name = models.CharField(max_length=20, default='')
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=50, default='')
    mobile = models.IntegerField( default=0)
    country = models.CharField(max_length=255, default=None)
    state = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255, default=None)
    address = models.CharField(max_length=255, default=None)
    image = models.ImageField(upload_to='pics')
    created = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=50,default=None,null=True)
    lat = models.CharField(max_length=250,default=None,null=True)





    def __str__(self):
        return self.name

class Country(models.Model):
    c_name=models.CharField(max_length=100)
    def __str__(self):
        return self.c_name

class State(models.Model):
    s_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.s_name


class City(models.Model):
    city_name = models.CharField(max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name
