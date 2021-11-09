from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (PatientSerializer, PatientSerilaSerializer, PrescriptionSerializer, MedicineForPrescriptionSerializer, 
                        TestForPrescriotionSerializer, HistorySerializer, HistoryCreateSerializer)
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Patient, Prescription, MedicineForPrescription, TestForPrescriotion, History
from django.db.models import Q
# Create your views here.

class PatientSerialView(APIView):
    
    def get(self, request, phoneNumber):
        phoneNumber = phoneNumber.strip()
        
        queryset = Patient.objects.filter(Q(contactNumber__icontains=phoneNumber))
        serializer_data = PatientSerializer(queryset, many=True)
        
        if serializer_data.data:
            return Response(serializer_data.data)
        else:
            return Response({'Message': 'No_Patient_found'})

    def post(self, request, phoneNumber):

        serializer_data = PatientSerilaSerializer(data=request.data)
        if serializer_data.is_valid():
            new_doctor = serializer_data.save()
            if new_doctor:
                content = {'message': 'New_Patient_Serial_Created'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)



class PatientHistoryView(APIView):
    
    def get(self, request, phoneNumber, userID, chemberID):
        
        phoneNumber = phoneNumber.strip()
        userID = userID.strip()
        chemberID = chemberID.strip()
        queryset = History.objects.filter(Q(patient__contactNumber__icontains=phoneNumber), 
                                          Q(user__id__icontains=userID),
                                          Q(chember__id__icontains=chemberID))
        serializer_data = HistorySerializer(queryset, many=True)
        
        if serializer_data.data:
            return Response(serializer_data.data)
        else:
            return Response({'Message': 'No_Patient_History_found'})

    def post(self, request, phoneNumber):

        serializer_data = HistoryCreateSerializer(data=request.data)
        if serializer_data.is_valid():
            new_doctor = serializer_data.save()
            if new_doctor:
                content = {'message': 'New_Patient_History_Created'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)