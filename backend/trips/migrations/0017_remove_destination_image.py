# Generated by Django 5.1 on 2024-09-28 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0016_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='image',
        ),
    ]