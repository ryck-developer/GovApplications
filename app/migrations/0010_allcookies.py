# Generated by Django 4.2 on 2023-05-08 14:37

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllCookies',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cookie', models.CharField(max_length=255, verbose_name='cookies gerados')),
            ],
            options={
                'verbose_name': 'cookie',
                'verbose_name_plural': 'cookies',
            },
        ),
    ]