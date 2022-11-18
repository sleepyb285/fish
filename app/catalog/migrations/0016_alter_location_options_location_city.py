# Generated by Django 4.1.3 on 2022-11-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_location_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['city']},
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(help_text='Населенный пункт', max_length=255, null=True),
        ),
    ]