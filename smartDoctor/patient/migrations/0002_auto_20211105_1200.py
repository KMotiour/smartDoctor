# Generated by Django 3.2.9 on 2021-11-05 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_alter_doctorinfo_doctorname'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicineforprescription',
            name='medicine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_medicine', to='Doctor.loaclmedicine'),
        ),
        migrations.AddField(
            model_name='testforprescriotion',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_text', to='Doctor.localtest'),
        ),
    ]