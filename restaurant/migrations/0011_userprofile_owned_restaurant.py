# Generated by Django 4.1.5 on 2023-01-28 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_remove_restaurant_photo_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='owned_restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restaurant'),
        ),
    ]
