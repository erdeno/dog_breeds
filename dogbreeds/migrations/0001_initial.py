# Generated by Django 3.1.5 on 2021-01-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('link', models.CharField(max_length=64)),
                ('smimg', models.CharField(max_length=64)),
                ('bigimg', models.CharField(max_length=64)),
            ],
        ),
    ]
