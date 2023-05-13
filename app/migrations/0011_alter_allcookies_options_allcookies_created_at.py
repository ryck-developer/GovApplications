# Generated by Django 4.2 on 2023-05-08 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_allcookies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allcookies',
            options={'ordering': ['-pk'], 'verbose_name': 'cookie', 'verbose_name_plural': 'cookies'},
        ),
        migrations.AddField(
            model_name='allcookies',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
    ]
