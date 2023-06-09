# Generated by Django 4.1.7 on 2023-04-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_activities_notes_alter_destination_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='notes',
            field=models.TextField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='destination',
            name='date',
            field=models.DateField(default='', verbose_name='Trip Date'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='notes',
            field=models.TextField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]
