# Generated by Django 4.1.5 on 2023-01-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_alter_cartitem_quantity_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='photo',
            field=models.ImageField(default='', upload_to='restaurant_photos'),
            preserve_default=False,
        ),
    ]
