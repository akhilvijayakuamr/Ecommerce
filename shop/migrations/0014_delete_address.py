# Generated by Django 4.1.2 on 2022-11-29 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_delete_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]