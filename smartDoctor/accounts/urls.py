from django.urls import path, include
from .views import CreateDoctorView, CreateAssistanceView, ChangePasswordView

urlpatterns = [
    path('create-doctor/', CreateDoctorView.as_view(), name='createDoctor'),
    path('create-assistance/', CreateAssistanceView.as_view(), name='createAssistance'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password')

]