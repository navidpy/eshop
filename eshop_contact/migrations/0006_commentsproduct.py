# Generated by Django 3.2 on 2021-04-27 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_products', '0010_product_visit_count'),
        ('eshop_contact', '0005_delete_commentsproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='متن پیام ')),
                ('publish', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='زمان انتشار')),
                ('accepted', models.BooleanField(verbose_name='تایید شده / نشده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام و نام خانوادگی ')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت های محصولات',
            },
        ),
    ]
