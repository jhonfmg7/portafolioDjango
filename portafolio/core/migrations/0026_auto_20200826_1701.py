# Generated by Django 3.0.5 on 2020-08-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20200826_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Numero de Contacto'),
        ),
    ]