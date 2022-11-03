# Generated by Django 4.1.3 on 2022-11-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_good_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.IntegerField(help_text='Введите стоимость рыбы', null=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='location',
            field=models.CharField(blank=True, choices=[('Б', 'Балтика'), ('А', 'Атлантический океан'), ('Л', 'Лужа'), ('У', 'АквариУм')], help_text='Выберите источник рыбы', max_length=1),
        ),
    ]
