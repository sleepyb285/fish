# Generated by Django 4.1.3 on 2022-11-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_alter_attribute_createdate_alter_category_createdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback_request',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]