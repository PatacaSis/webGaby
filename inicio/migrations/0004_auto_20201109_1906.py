# Generated by Django 3.0 on 2020-11-09 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20201104_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeria',
            old_name='proyecto',
            new_name='proyecto_id',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='descripcion',
        ),
    ]