# Generated by Django 3.0.5 on 2020-08-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200821_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('career', models.CharField(max_length=100, verbose_name='Profesión')),
                ('facebook', models.URLField(verbose_name='facebook')),
                ('twitter', models.URLField(verbose_name='twitter')),
                ('linkedin', models.URLField(verbose_name='linkedin')),
                ('another', models.URLField(verbose_name='another')),
            ],
        ),
    ]