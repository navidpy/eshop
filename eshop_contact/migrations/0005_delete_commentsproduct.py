# Generated by Django 3.2 on 2021-04-27 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_contact', '0004_alter_commentsproduct_publish'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentsProduct',
        ),
    ]