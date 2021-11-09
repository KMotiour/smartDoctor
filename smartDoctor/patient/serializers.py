from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Patient, Prescription, MedicineForPrescription, TestForPrescriotion, History
from chember.serializers import ChemberSerializer
from Doctor.serializers import DoctorInfoSerializer, LoaclMedicineSerializer, LocalTestSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class PatientSerializer(serializers.ModelSerializer):
    chember = ChemberSerializer()
    class Meta:
        model = Patient
        fields = ['chember', 'name', 'contactNumber', 'age', 'gender']
        
class PatientSerilaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = ['chember', 'name', 'contactNumber', 'age', 'gender']

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model = Prescription
        fields = ['patient', 'descrioption']

class MedicineForPrescriptionSerializer(serializers.ModelSerializer):
    prescription = PrescriptionSerializer()
    medicine = LoaclMedicineSerializer()
    class Meta:
        model = MedicineForPrescription
        fields = ['prescription', 'medicine',  'howManyDays',  'howManyTimes']

class TestForPrescriotionSerializer(serializers.ModelSerializer):
    prescription = PrescriptionSerializer()
    test = LocalTestSerializer()
    class Meta:
        model = TestForPrescriotion
        fields = ['test', 'prescription',  'description']


class HistorySerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    chember = ChemberSerializer()
    user = get_user_model()
    class Meta:
        model = History
        fields = ['patient', 'chember',  'user',  'log', 'date']

class HistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['patient', 'chember',  'user',  'log']