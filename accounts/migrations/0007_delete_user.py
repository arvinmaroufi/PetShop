# Generated by Django 5.1.4 on 2025-01-19 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_bio_user_about_me'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
