# Generated by Django 3.2.16 on 2022-11-26 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdetail', '0003_auto_20221123_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='location',
        ),
    ]