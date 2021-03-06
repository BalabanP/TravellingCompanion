# Generated by Django 3.2.2 on 2021-10-15 08:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('budget', models.PositiveIntegerField()),
                ('currency', models.CharField(choices=[('Lei', 'Leu Romanesc'), ('EUR', 'Euro'), ('USD', 'Dolar American'), ('GBP', 'U.K. Pound')], default='Lei', max_length=7)),
                ('comments', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=datetime.datetime.now)),
                ('time_from', models.TimeField(default=datetime.datetime.now)),
                ('date_to', models.DateField(default=datetime.datetime.now)),
                ('time_to', models.TimeField(default=datetime.datetime.now)),
                ('price', models.PositiveIntegerField()),
                ('currency', models.CharField(choices=[('Lei', 'Leu Romanesc'), ('EUR', 'Euro'), ('USD', 'Dolar American'), ('GBP', 'U.K. Pound')], default='Lei', max_length=7)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='travelling_companion_app.location')),
                ('origin_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='travelling_companion_app.location')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion_app.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=datetime.datetime.now)),
                ('time_from', models.TimeField(default=datetime.datetime.now)),
                ('date_to', models.DateField(default=datetime.datetime.now)),
                ('time_to', models.TimeField(default=datetime.datetime.now)),
                ('price', models.PositiveIntegerField()),
                ('currency', models.CharField(choices=[('Lei', 'Leu Romanesc'), ('EUR', 'Euro'), ('USD', 'Dolar American'), ('GBP', 'U.K. Pound')], default='Lei', max_length=7)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion_app.location')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion_app.trip')),
            ],
        ),
    ]
