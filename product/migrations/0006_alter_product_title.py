# Generated by Django 5.1.4 on 2025-01-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_comment_popular_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, unique=True, verbose_name='عنوان محصول'),
        ),
    ]
