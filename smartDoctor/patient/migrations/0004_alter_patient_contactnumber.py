# Generated by Django 3.2.9 on 2021-11-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_prescription_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='contactNumber',
            field=models.CharField(max_length=50, verbose_name='Contact Number'),
        ),
    ]
