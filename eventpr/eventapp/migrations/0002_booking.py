# Generated by Django 4.2.19 on 2025-02-13 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=50)),
                ('cus_mob', models.CharField(max_length=12)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event')),
            ],
        ),
    ]
