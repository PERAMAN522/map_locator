# Generated by Django 3.2.16 on 2022-11-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetail', '0004_remove_userdetails_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
