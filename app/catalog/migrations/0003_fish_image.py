# Generated by Django 4.1.3 on 2022-11-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_provider_fish_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='FishImages/%Y/%m/%d/'),
        ),
    ]