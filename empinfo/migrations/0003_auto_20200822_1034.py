# Generated by Django 3.0.8 on 2020-08-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empinfo', '0002_auto_20200822_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(to='empinfo.Employee'),
        ),
    ]
