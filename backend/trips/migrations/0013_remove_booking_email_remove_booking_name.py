# Generated by Django 5.1 on 2024-09-26 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0012_remove_booking_check_in_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
    ]
