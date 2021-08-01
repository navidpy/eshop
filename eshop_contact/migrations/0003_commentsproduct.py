# Generated by Django 3.2 on 2021-04-23 15:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0010_product_visit_count'),
        ('eshop_contact', '0002_alter_contactus_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, verbose_name='نام و نام خانوادگی ')),
                ('email', models.EmailField(max_length=35, verbose_name='ایمیل ')),
                ('text', models.TextField(max_length=500, verbose_name='متن پیام ')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('accepted', models.BooleanField(verbose_name='تایید شده / نشده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت های محصولات',
            },
        ),
    ]
