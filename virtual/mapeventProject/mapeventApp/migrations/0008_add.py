# Generated by Django 4.0.5 on 2022-06-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeventApp', '0007_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=122)),
                ('box', models.CharField(max_length=122)),
            ],
        ),
    ]