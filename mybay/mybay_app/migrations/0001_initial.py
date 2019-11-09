# Generated by Django 2.2.6 on 2019-11-09 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=512, verbose_name='name')),
                ('item_category', models.CharField(max_length=512, verbose_name='category')),
                ('item_price', models.FloatField(verbose_name='price')),
                ('item_country', models.CharField(max_length=512)),
                ('item_date', models.DateField(auto_now_add=True)),
                ('item_pic', models.ImageField(upload_to='images', verbose_name="item's Picture")),
            ],
            options={
                'verbose_name': 'item List',
                'verbose_name_plural': 'item List',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=512, verbose_name='name')),
                ('item_category', models.CharField(max_length=512, verbose_name='category')),
                ('item_price', models.FloatField(verbose_name='price')),
                ('item_date', models.DateField(auto_now_add=True)),
                ('item_pic', models.ImageField(upload_to='images', verbose_name="item's Picture")),
                ('item_country', models.CharField(max_length=512)),
                ('item_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mybay_app.Item')),
                ('item_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mybay_app.Profile', verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mybay_app.Profile', verbose_name='user'),
        ),
    ]
