# Generated by Django 3.1.3 on 2021-04-24 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunafa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kunafa',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
