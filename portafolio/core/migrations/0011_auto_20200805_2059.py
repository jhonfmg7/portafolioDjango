# Generated by Django 3.0.5 on 2020-08-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_choose'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choose',
            options={'verbose_name': 'Elección', 'verbose_name_plural': 'Elecciones'},
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='video', verbose_name='Imagen video'),
        ),
    ]
