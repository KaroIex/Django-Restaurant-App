# Generated by Django 4.1.5 on 2023-01-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_restaurant_phone_number_restaurant_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='photo',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(null=True, upload_to='product-img/'),
        ),
    ]
