# Generated by Django 3.2 on 2021-04-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapp', '0012_auto_20210427_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='labor_Phone',
            field=models.IntegerField(max_length=15, verbose_name='連絡電話'),
        ),
    ]
