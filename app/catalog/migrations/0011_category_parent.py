# Generated by Django 4.1.3 on 2022-11-15 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_fish_attributes_alter_filterinfo_rel_attribute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='catalog.category'),
        ),
    ]
