# Generated by Django 4.1.3 on 2022-11-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_provider_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
