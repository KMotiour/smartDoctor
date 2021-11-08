from django.db.models import query
from django.db.models import Q
from Doctor import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChemberSerializer, ChemberSettingsSerializer, ChemberScheduleSerializer, ChemberSerializerExtra
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Chember, Settings, ChemberSchedule
# Create your views here.


class ChemberView(APIView):
    # serializer_class = ChemberSerializer
    def get(self, request, chember):
        serializer_data = ChemberSerializer(Chember.objects.filter(chamber_name__icontains=chember) ,many=True)
        if serializer_data.data:
            return Response(serializer_data.data)
        else:
            return Response({'Message': 'No_chember_found'})

    def post(self, request, chember):
        print(chember)
        serializer_data = ChemberSerializerExtra(data=request.data)
        if serializer_data.is_valid():
            new_chember = serializer_data.save()
            if new_chember:
                content = {'message': 'new_chember_created'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)



class ChemberRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChemberSerializerExtra
    queryset = Chember.objects.all()
    
class ChemberSettingsRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChemberSettingsSerializer
    queryset = Settings.objects.all() 
    

class ChemberScheduleRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChemberSettingsSerializer
    queryset = Settings.objects.all()
   
    