# Generated by Django 5.0.7 on 2024-11-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asientos',
            name='id_asiento',
            field=models.IntegerField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
