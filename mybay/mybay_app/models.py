from django.db import models

class AppUser(models.Model):
    user_email = models.CharField(unique=True, max_length=512, verbose_name="email")
    user_pass = models.CharField(max_length=512, verbose_name="password")
    user_country = models.CharField(max_length=512, verbose_name="country")

    class Meta:
        verbose_name = 'user List'
        verbose_name_plural = 'user List'
        db_table = 'app_user'

class AppItem(models.Model):
    item_name = models.CharField(max_length=512, verbose_name="name")
    item_category = models.CharField(max_length=512, verbose_name="category")
    item_price = models.IntegerField(verbose_name="price")
    item_date = models.DateField(auto_now_add=True, blank=True)
    item_pic = models.BinaryField(verbose_name="item's Picture")
    item_owner = models.ForeignKey('AppUser', on_delete = models.CASCADE, verbose_name="user")

    class Meta:
        verbose_name = 'item List'
        verbose_name_plural = 'item List'
        db_table = 'app_item'
