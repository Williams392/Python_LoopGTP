# Generated by Django 4.2.1 on 2023-05-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_synopsis_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=None, max_length=255, null=True, unique=True),
        ),
    ]