# Generated by Django 4.1.3 on 2022-11-28 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_alter_fish_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback_generic',
            options={'ordering': ['-date']},
        ),
    ]