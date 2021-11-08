from rest_framework import serializers
from .models import Chember, ChemberSchedule, Settings



class ChemberSerializerExtra(serializers.ModelSerializer):
    class Meta:
        model = Chember
        fields = ['chamber_name', 'location', 'contact',]
      


class ChemberSettingsSerializer(serializers.ModelSerializer):
    chember  = ChemberSerializerExtra()
    class Meta:
        model = Settings
        fields = ['chember', 'patinetLimit', 'SerialLimitForOneContactNumber', 'patientAccountLimitForOneNumber', 
                    'indexingForLateCommer', 'indexingForReportShower', 'isSendMessage']


class ChemberScheduleSerializer(serializers.ModelSerializer):
    chember = ChemberSerializerExtra()
    class Meta:
        model  = ChemberSchedule
        fields = ['chember', 'day', 'startTime', 'endTime']

class ChemberSerializer(serializers.ModelSerializer):
    chember_settings = ChemberSettingsSerializer()
    chember_schedule = ChemberScheduleSerializer(many=True)
    class Meta:
        model = Chember
        fields = ['chamber_name', 'location', 'contact', 'chember_settings', 'chember_schedule']
        extra_kwargs = {'chember_settings': {'read_only': True}, 'chember_schedule':{'read_only': True}}

