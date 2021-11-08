from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorInfoSerializer, LoaclMedicineSerializer, LocalTestSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import DoctorInfo, LoaclMedicine, LocalTest
from django.db.models import Q
# Create your views here.

    
class DoctorInfoView(APIView):
    # serializer_class = ChemberSerializer
    def get(self, request):
        serializer_data = DoctorInfoSerializer(DoctorInfo.objects.first())
        if serializer_data.data:
            return Response(serializer_data.data)
        else:
            return Response({'Message': 'No_Doctor_found'})

    def post(self, request):

        serializer_data = DoctorInfoSerializer(data=request.data)
        if serializer_data.is_valid():
            new_doctor = serializer_data.save()
            if new_doctor:
                content = {'message': 'new_Doctor_created'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class GetLoaclaMedicine(ListCreateAPIView):
    serializer_class = LoaclMedicineSerializer
    def get_queryset(self):
        medicineName = self.kwargs.get('medicineName').strip()
        if medicineName:
            return LoaclMedicine.objects.filter(Q(medicineName__icontains=medicineName))
        else:
            return LoaclMedicine.objects.all()

class CreateLocalMedicine(APIView):
    
    def post(self, request):
        print(request.data)
        serializer_data = LoaclMedicineSerializer(data=request.data)
        if serializer_data.is_valid():
            new_medicine = serializer_data.save()
            if new_medicine:
                content = {'message': 'new_Medicine_Added_to_local_medicine_table'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

class GetLoaclaTest(ListCreateAPIView):
    serializer_class = LocalTestSerializer
    def get_queryset(self):
        testName = self.kwargs.get('testName').strip()
        print(testName)
        if testName:
            return  LocalTest.objects.filter(testName__icontains=testName)
        else:
            return LocalTest.objects.all()

class CreateLocalTest(APIView):
    
    def post(self, request):
        serializer_data = LocalTestSerializer(data=request.data)
        if serializer_data.is_valid():
            new_Test = serializer_data.save()
            if new_Test:
                content = {'message': 'new_Test_Added_to_local_Test_table'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
