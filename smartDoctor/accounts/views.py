from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import UpdateAPIView
from .serializers import CreateDoctorSerializer, CreateAssistanceSerializer, ChangePasswordSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

# Create Doctor 
class CreateDoctorView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer_data = CreateDoctorSerializer(data=request.data)
        if serializer_data.is_valid():
            new_user = serializer_data.save()
            if new_user:
                content = {'message': 'new user created'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


# Create Doctor 
class CreateAssistanceView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer_data = CreateAssistanceSerializer(data=request.data)
        if serializer_data.is_valid():
            new_user = serializer_data.save()
            if new_user:
                content = {'message': 'new user created'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)