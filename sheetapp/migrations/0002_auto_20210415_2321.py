# Generated by Django 3.2 on 2021-04-15 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='location',
            new_name='labor_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
