# Generated by Django 4.1.7 on 2023-04-10 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_photo_options_alter_photo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='time',
            field=models.TimeField(default=datetime.time(12, 17, 42, 751754)),
        ),
    ]
