from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_country = models.CharField(max_length=512)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class AppItem(models.Model):
    item_name = models.CharField(max_length=512, verbose_name="name")
    item_category = models.CharField(max_length=512, verbose_name="category")
    item_price = models.IntegerField(verbose_name="price")
    item_date = models.DateField(auto_now_add=True, blank=True)
    item_pic = models.ImageField(verbose_name="item's Picture", upload_to = 'media/')
    item_owner = models.ForeignKey('Profile', on_delete = models.CASCADE, verbose_name="user")

    class Meta:
        verbose_name = 'item List'
        verbose_name_plural = 'item List'
        db_table = 'app_item'
    
    def __str__(self):
        return self.item_name
