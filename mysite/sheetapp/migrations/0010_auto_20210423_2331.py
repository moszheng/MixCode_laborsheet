# Generated by Django 3.2 on 2021-04-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapp', '0009_remove_post_labor_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='labor_signature',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category_choice',
            field=models.CharField(choices=[('9A', '9A 執行業務所得'), ('9B', '9B 稿費')], default='9A', max_length=3, verbose_name='申報類別'),
        ),
        migrations.AlterField(
            model_name='post',
            name='labor_email',
            field=models.EmailField(max_length=60, verbose_name='電子信箱'),
        ),
        migrations.AlterField(
            model_name='post',
            name='member_choice',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=3, verbose_name='職業工業會員'),
        ),
    ]
