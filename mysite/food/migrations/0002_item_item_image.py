# Generated by Django 3.1.6 on 2021-05-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://comicrazy.co.uk/wp-content/plugins/bigcommerce/assets/img/public/bc-product-placeholder.jpg', max_length=500),
        ),
    ]