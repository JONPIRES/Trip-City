# Generated by Django 4.1.7 on 2023-04-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_photo_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='comment',
            field=models.TextField(default='hi', max_length=250),
        ),
    ]