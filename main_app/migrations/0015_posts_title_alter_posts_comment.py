# Generated by Django 4.1.7 on 2023-04-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_posts_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='posts',
            name='comment',
            field=models.TextField(max_length=250),
        ),
    ]