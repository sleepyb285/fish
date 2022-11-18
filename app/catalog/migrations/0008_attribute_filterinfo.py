# Generated by Django 4.1.3 on 2022-11-15 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_provider_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название атрибута', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FilterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Введите значение', max_length=255)),
                ('rel_attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.attribute')),
                ('rel_fish', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.fish')),
            ],
        ),
    ]