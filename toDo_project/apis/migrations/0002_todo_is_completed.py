# Generated by Django 4.1.1 on 2022-09-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
