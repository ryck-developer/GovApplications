# Generated by Django 4.2 on 2023-05-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('ADHEART', 'Adheart'), ('ADSPY', 'Adspy'), ('ADVAULT', 'Advault'), ('PIPIADS', 'Pipiads'), ('BISPY', 'Bispy')], max_length=100, verbose_name='Nome'),
        ),
    ]