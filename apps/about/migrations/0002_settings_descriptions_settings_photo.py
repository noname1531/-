# Generated by Django 5.0.4 on 2024-04-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='descriptions',
            field=models.TextField(default=1, verbose_name='Описание сайта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='photo',
            field=models.ImageField(default=1, upload_to='logo/image', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]