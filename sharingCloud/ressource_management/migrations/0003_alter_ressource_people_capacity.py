# Generated by Django 4.0.4 on 2022-04-17 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressource_management', '0002_alter_ressource_localization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='people_capacity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='capacité'),
        ),
    ]
