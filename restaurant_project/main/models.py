from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    item = models.ManyToManyField(Item)
    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, null=True)
    menu = models.ForeignKey(Menu, null=True)
    cuisine = models.CharField(max_length=255, null=True)
    hours = models.TextField(null=True)
    number = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    owner = models.OneToOneField(Restaurant, null=True)
    number = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=128, null=True)
    zip_code = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    allergies = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(UserProfile)
    date = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    notes = models.CharField(max_length=512, blank=True, null=True)
    number = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=128, null=True)
    zip_code = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


