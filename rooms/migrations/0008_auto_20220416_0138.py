# Generated by Django 2.2.5 on 2022-04-15 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20220416_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
    ]
