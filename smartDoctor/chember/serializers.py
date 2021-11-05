from rest_framework import serializers
from .models import Chember, ChemberSchedule, Settings


class ChemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chember
        fields = ['chamber_name', 'location', 'contact']



class ChemberSettingsSerializer(serializers.ModelSerializer):
    chember  = ChemberSerializer()
    class Meta:
        model = Settings
        fields = ['chember', 'patinetLimit', 'SerialLimitForOneContactNumber', 'patientAccountLimitForOneNumber', 
                    'indexingForLateCommer', 'indexingForReportShower', 'isSendMessage']


class ChemberScheduleSerializer(serializers.ModelSerializer):
    chember = ChemberSerializer()
    class Meta:
        model  = ChemberSchedule
        fields = ['chember', 'day', 'startTime', 'endTime']