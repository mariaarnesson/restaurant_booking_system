# Generated by Django 3.2.19 on 2023-07-09 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20230704_0942'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='onlinebooking',
            unique_together=set(),
        ),
    ]