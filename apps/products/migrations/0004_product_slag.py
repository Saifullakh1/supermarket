# Generated by Django 3.2.4 on 2021-06-21 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slag',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
