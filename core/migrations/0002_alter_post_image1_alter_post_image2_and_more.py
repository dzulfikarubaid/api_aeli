# Generated by Django 4.2.3 on 2023-07-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, default='', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image5',
            field=models.ImageField(blank=True, default='', upload_to='images/%Y/%m/%d'),
        ),
    ]
