# Generated by Django 2.2.5 on 2022-04-14 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20220414_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='houserules',
            new_name='house_rules',
        ),
    ]
