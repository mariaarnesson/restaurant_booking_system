# Generated by Django 3.2.19 on 2023-07-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20230630_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinebooking',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='onlinebooking',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
