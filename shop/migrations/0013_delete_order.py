# Generated by Django 4.1.2 on 2022-11-25 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_address_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]