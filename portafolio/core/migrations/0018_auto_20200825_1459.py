# Generated by Django 3.0.5 on 2020-08-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='another',
            field=models.URLField(blank=True, null=True, verbose_name='another'),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='linkedin'),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='twitter'),
        ),
    ]
