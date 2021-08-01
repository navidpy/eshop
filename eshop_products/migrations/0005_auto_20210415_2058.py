# Generated by Django 3.2 on 2021-04-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_auto_20210415_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='لینک'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(max_length=60, null='d', verbose_name='تگ ها (با "." جدا کنید)'),
            preserve_default='d',
        ),
    ]
