# Generated by Django 4.2.3 on 2023-07-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_donasi_jual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jual',
            name='harga',
            field=models.TextField(),
        ),
    ]