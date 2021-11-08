from django.urls import path, include
from .views import DoctorInfoView, GetLoaclaMedicine, CreateLocalMedicine, GetLoaclaTest, CreateLocalTest 


urlpatterns = [

    path("", DoctorInfoView.as_view(), name="DoctorInfo"),
    path("getLocalMedicine/<str:medicineName>/", GetLoaclaMedicine.as_view(), name="GetLoaclaMedicine"),
    path("createLocalMedicine/", CreateLocalMedicine.as_view(), name="CreateLocalMedicine"),
    path("getLoaclaTest/<str:testName>/", GetLoaclaTest.as_view(), name="GetLoaclaTest"),
    path("createLocalTest/", CreateLocalTest.as_view(), name="CreateLocalTest")


] 