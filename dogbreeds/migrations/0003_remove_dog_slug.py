# Generated by Django 3.1.5 on 2021-01-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogbreeds', '0002_dog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='slug',
        ),
    ]