# Generated by Django 4.0.4 on 2022-04-17 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressource_management', '0003_alter_ressource_people_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='people_capacity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='capacité'),
        ),
    ]