# Generated by Django 4.1.3 on 2022-11-03 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_alter_category_name_delete_good_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите место вылова рыбы', max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-price']},
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.location'),
        ),
    ]
