from django.db import models

# Create your models here.

# model for a movie
class Movies(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_date = models.PositiveIntegerField()
    director = models.CharField(max_length=400)
    
    # string representation of an object 
    def __str__(self):
        return self.title

# modle for a customer
class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()
    
    # string representation of an object
    def __str__(self):
        return self.first_name  +  " "  + self.last_name

