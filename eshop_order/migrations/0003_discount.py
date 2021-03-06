# Generated by Django 3.2 on 2021-04-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0002_order_trackingcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='کد')),
                ('percentage', models.IntegerField(verbose_name='درصد تخفیف')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
                ('total', models.IntegerField(verbose_name='تعداد مجاز استفاده')),
                ('count', models.IntegerField(default=0, verbose_name='تعداد استفاده شده')),
            ],
        ),
    ]
