# Generated by Django 3.2.9 on 2021-11-04 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chember', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('contactNumber', models.IntegerField(verbose_name='Contact Number')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(max_length=50, verbose_name='Gender')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('chember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chember_patient', to='chember.chember')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrioption', models.CharField(max_length=50, verbose_name='Drescrioption')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_prescription', to='patient.patient')),
            ],
        ),
        migrations.CreateModel(
            name='TestForPrescriotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prescription_text', to='patient.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineForPrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('howManyDays', models.IntegerField(default=0, verbose_name='How Many Days')),
                ('howManyTimes', models.CharField(max_length=50, verbose_name='How Many Days')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescripton_medicine', to='patient.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=500, verbose_name='Log')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('chember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chember_patient_history', to='chember.chember')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_history', to='patient.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='accounts.newusers')),
            ],
        ),
    ]
