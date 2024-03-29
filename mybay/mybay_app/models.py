from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_country = CountryField()

    def __str__(self):
        return self.user.username


class Item(models.Model):
    item_name = models.CharField(max_length=512, verbose_name="name")
    item_category = models.CharField(max_length=512, verbose_name="category")
    item_price = models.FloatField(verbose_name="price")
    item_country = CountryField()
    item_date = models.DateField(auto_now_add=True, blank=True)
    item_pic = models.ImageField(verbose_name="item's Picture", upload_to = 'images')
    item_owner = models.ForeignKey('Profile', on_delete = models.CASCADE, verbose_name="user")

    class Meta:
        verbose_name = 'item List'
        verbose_name_plural = 'item List'
    
    def __str__(self):
        return self.item_name

class ItemEdit(models.Model):
    item_name = models.CharField(max_length=512, verbose_name="name")
    item_category = models.CharField(max_length=512, verbose_name="category")
    item_price = models.FloatField(verbose_name="price")
    item_date = models.DateField(auto_now_add=True, blank=True)
    item_pic = models.ImageField(verbose_name="item's Picture", upload_to='images')
    item_owner = models.ForeignKey('Profile', on_delete = models.CASCADE, verbose_name="user")
    item_country = CountryField()
    item_list = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_name
