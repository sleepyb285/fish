# Generated by Django 4.1.3 on 2022-11-21 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_alter_callback_request_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
