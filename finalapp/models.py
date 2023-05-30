from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    c_name=models.CharField(max_length=255)
    c_image=models.ImageField(upload_to="image/",null=True)
class Foods(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    f_name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    qty=models.IntegerField()
    price=models.IntegerField()
    f_image=models.ImageField(upload_to="image/",null=True)
class Events(models.Model):
    e_name=models.CharField(max_length=255)
    e_image=models.ImageField(upload_to="image/",null=True)
class Customer(models.Model):
    userc=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    image=models.ImageField(upload_to="image/",null=True)
class Eventbooking(models.Model):
    eventname=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=200)
    people=models.IntegerField()
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    eventpack=models.ForeignKey(Events,on_delete=models.CASCADE)
    menupack=models.ForeignKey(Foods,on_delete=models.CASCADE)
    amount=models.CharField(max_length=255)
    approved=models.BooleanField(default=False)
    completed=models.BooleanField(default=False)
    reason=models.CharField(max_length=255,blank=True,null=True)
    feedback=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.eventname
class Foodbooking(models.Model):
    date=models.DateField()
    time=models.TimeField()
    people=models.IntegerField()
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    catpack=models.ForeignKey(Category,on_delete=models.CASCADE)
    menupack=models.ForeignKey(Foods,on_delete=models.CASCADE)
    amount=models.CharField(max_length=255)
    approved=models.BooleanField(default=False)
    completed=models.BooleanField(default=False)
    reason=models.CharField(max_length=255,blank=True,null=True)
    feedback=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.foodname    