# Generated by Django 4.1.2 on 2022-10-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile_cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='mobiles')),
                ('name', models.CharField(max_length=30)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('camera', models.IntegerField()),
                ('battary', models.IntegerField()),
                ('charging_speed', models.IntegerField()),
                ('processor', models.IntegerField()),
            ],
        ),
    ]
