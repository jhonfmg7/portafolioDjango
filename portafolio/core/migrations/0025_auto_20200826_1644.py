# Generated by Django 3.0.5 on 2020-08-26 16:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_video_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='content_2',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True, verbose_name='Contenido de texto'),
        ),
        migrations.AddField(
            model_name='video_2',
            name='content_2',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True, verbose_name='Contenido de texto'),
        ),
    ]
