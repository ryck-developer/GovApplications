# Generated by Django 4.2 on 2023-05-04 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_browser_user_device_user_ip_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='browser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='device',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ip_adress',
        ),
    ]