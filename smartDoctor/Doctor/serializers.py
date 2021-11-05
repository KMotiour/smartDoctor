from django.db.models import fields
from rest_framework import serializers
from .models import DoctorInfo, LoaclMedicine, LocalTest

class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = ['doctorName', 'doctorTitle', 'phoneNumber', 'speciality', 'blog', 'image']
    

class LoaclMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoaclMedicine
        fields = ['medicineName', 'medicineType', 'companyNem',]


class LocalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalTest
        fields = ['testName', 'type', 'description',]