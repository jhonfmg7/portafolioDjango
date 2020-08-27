# Generated by Django 3.0.5 on 2020-08-21 16:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_project_relevance'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True, verbose_name='Contenido de texto'),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo de texto'),
        ),
    ]