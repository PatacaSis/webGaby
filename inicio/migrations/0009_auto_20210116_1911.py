# Generated by Django 3.0 on 2021-01-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_auto_20210116_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='img',
            field=models.ImageField(null=True, upload_to='imagenes/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='img_principal',
            field=models.ImageField(blank=True, null=True, upload_to='principales/%Y/%m/%d'),
        ),
    ]