# Generated by Django 4.1.7 on 2023-04-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_activities_notes_destination_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='rating',
            field=models.CharField(choices=[('1', '*'), ('2', '* *'), ('3', '* * *'), ('4', '* * * *'), ('5', '* * * * *')], default='1', max_length=1),
        ),
    ]
