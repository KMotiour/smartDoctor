from django.urls import path, include
from .views import PatientSerialView, PatientHistoryView


urlpatterns = [

    path("serial/<str:phoneNumber>/", PatientSerialView.as_view(), name="PatientSerialView"),
    path("history/<str:phoneNumber>/<str:userID>/<str:chemberID>/", PatientHistoryView.as_view(), name="PatientHistoryView"),

] 