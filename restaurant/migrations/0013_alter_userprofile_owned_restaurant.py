# Generated by Django 4.1.5 on 2023-01-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_remove_userprofile_owned_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='owned_restaurant',
            field=models.ManyToManyField(blank=True, null=True, related_name='owned_by', to='restaurant.restaurant'),
        ),
    ]
