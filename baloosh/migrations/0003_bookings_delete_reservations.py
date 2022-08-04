# Generated by Django 4.0.6 on 2022-08-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baloosh', '0002_reservations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivaldates', models.CharField(max_length=200)),
                ('departuredates', models.CharField(max_length=200)),
                ('adults', models.CharField(max_length=200)),
                ('children', models.CharField(max_length=200)),
                ('noofrooms', models.CharField(max_length=200)),
                ('roomtypes', models.CharField(max_length=200)),
                ('amounts', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
    ]
