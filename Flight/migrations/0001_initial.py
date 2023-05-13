# Generated by Django 4.0.1 on 2023-01-15 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Airline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('Flights_id', models.AutoField(primary_key=True, serialize=False)),
                ('Routes', models.CharField(max_length=500)),
                ('Dist_bet_airports', models.CharField(max_length=500)),
                ('arriving_time', models.CharField(max_length=100)),
                ('Departing_time', models.CharField(max_length=100)),
                ('total_ticket', models.IntegerField(default=0)),
                ('Airline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airline.airline')),
            ],
        ),
    ]