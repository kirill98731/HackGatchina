# Generated by Django 2.2.1 on 2019-05-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sight',
            name='work_end',
            field=models.TimeField(default='17:00:00'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='work_start',
            field=models.TimeField(default='08:00:00'),
        ),
    ]