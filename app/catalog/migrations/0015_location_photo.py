# Generated by Django 4.1.3 on 2022-11-18 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/locations/'),
        ),
    ]
