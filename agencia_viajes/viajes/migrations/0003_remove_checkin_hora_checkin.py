# Generated by Django 5.0.7 on 2024-11-21 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0002_alter_asientos_id_asiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='hora_checkin',
        ),
    ]
