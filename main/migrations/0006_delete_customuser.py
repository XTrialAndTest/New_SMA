# Generated by Django 4.2.1 on 2023-05-22 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_customuser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
