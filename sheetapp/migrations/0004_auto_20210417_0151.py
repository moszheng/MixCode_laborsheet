# Generated by Django 3.2 on 2021-04-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapp', '0003_auto_20210416_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='labor_bank',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='labor_bankaccount',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='labor_bankname',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='labor_location',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='project_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='labor_ID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='labor_Phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='labor_name',
            field=models.CharField(max_length=20),
        ),
    ]
