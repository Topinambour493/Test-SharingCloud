# Generated by Django 4.0.4 on 2022-04-14 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40)),
                ('localization', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=40)),
                ('people_capacity', models.IntegerField(default=0)),
            ],
        ),
    ]
