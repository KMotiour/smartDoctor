# Generated by Django 3.2.9 on 2021-11-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chember', '0003_auto_20211106_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemberschedule',
            name='endTime',
            field=models.TimeField(null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='chemberschedule',
            name='startTime',
            field=models.TimeField(null=True, verbose_name='Start Time'),
        ),
    ]
