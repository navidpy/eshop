# Generated by Django 3.2 on 2021-04-19 08:39

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0004_auto_20210419_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeaderSite', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر بالا جستوجو')),
                ('mapImage', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر نقشه تماس باما')),
                ('productImage', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر بالا محصولات')),
                ('advertiseImage', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر تبلیغات')),
                ('advertiseUrl', models.URLField(blank=True, null=True, verbose_name='لینک تبلیغ')),
                ('footerSite1', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر پایین سایت 1')),
                ('footerSite2', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر پایین سایت 2')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='ایکون مرورگر')),
            ],
            options={
                'verbose_name': 'تنظیمات تصاویر',
                'verbose_name_plural': 'مدیریت تصاویر سایت',
            },
        ),
    ]