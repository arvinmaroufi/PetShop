# Generated by Django 5.1.4 on 2025-01-19 00:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='درباره من'),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='شماره تلفن'),
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='تایید'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='پست الکترونیکی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='account/profile', verbose_name='تصویر پروفایل'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
