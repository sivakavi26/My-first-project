# Generated by Django 3.1.2 on 2020-11-30 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='cusomer',
            new_name='customer',
        ),
    ]
