# Generated by Django 5.1 on 2024-09-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0014_booking_check_in_date_booking_check_out_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guest_details',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='num_guests',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='num_rooms',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room_type',
        ),
    ]