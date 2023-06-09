# Generated by Django 4.2.1 on 2023-05-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug_from_lang',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('uz', 'Uzbek')], max_length=64, null=True, verbose_name='select the language of the slug'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='slug_from_lang',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('uz', 'Uzbek')], max_length=64, null=True, verbose_name='select the language of the slug'),
        ),
    ]
