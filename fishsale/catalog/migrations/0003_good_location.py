# Generated by Django 4.1.3 on 2022-11-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_goods_good'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='location',
            field=models.CharField(blank=True, choices=[('Б', 'Балтика'), ('А', 'Атлантический океан'), ('Л', 'Лужа'), ('У', 'АквариУм')], help_text='Где выловлена рыба', max_length=1),
        ),
    ]