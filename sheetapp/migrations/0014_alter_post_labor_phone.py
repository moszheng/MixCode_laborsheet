# Generated by Django 3.2 on 2021-04-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapp', '0013_alter_post_labor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='labor_Phone',
            field=models.CharField(max_length=15, verbose_name='連絡電話'),
        ),
    ]