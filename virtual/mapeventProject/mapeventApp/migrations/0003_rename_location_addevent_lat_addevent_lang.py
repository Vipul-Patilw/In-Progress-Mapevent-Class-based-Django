# Generated by Django 4.0.6 on 2022-08-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeventApp', '0002_alter_addevent_fromtime_alter_addevent_todate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addevent',
            old_name='location',
            new_name='lat',
        ),
        migrations.AddField(
            model_name='addevent',
            name='lang',
            field=models.CharField(default='', max_length=122),
        ),
    ]