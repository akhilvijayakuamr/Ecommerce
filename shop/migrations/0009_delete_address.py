# Generated by Django 4.1.2 on 2022-11-25 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
