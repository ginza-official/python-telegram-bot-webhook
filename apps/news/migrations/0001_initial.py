# Generated by Django 4.2.1 on 2023-05-19 06:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Folder',
                'verbose_name_plural': 'Folders',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
                ('slug_from_lang', models.CharField(blank=True, choices=[('en', 'English'), ('ru', 'Russian'), ('uz', 'Uzbek')], max_length=64, null=True, verbose_name='select the language of the slug')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('banner', models.ImageField(upload_to='banner/', verbose_name='Banner')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Conten')),
                ('published_at', models.DateField(verbose_name='Published at')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['-published_at'],
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
                ('slug_from_lang', models.CharField(blank=True, choices=[('en', 'English'), ('ru', 'Russian'), ('uz', 'Uzbek')], max_length=64, null=True, verbose_name='select the language of the slug')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Static Page',
                'verbose_name_plural': 'Static Pages',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Image')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.folder', verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
    ]
