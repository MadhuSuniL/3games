# Generated by Django 4.1.2 on 2022-11-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_gg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gg',
            name='img',
            field=models.FileField(upload_to='cc'),
        ),
    ]
