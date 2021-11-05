from django.db import models
from django.db.models.fields import TimeField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Chember(models.Model):
    chamber_name = models.CharField(max_length=500)
    location = models.CharField(max_length=1000, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)

class Settings(models.Model):
    chember = models.ForeignKey(Chember, related_name="chember_settings", on_delete=models.CASCADE)
    patinetLimit = models.IntegerField(_("Patient Limit"))
    SerialLimitForOneContactNumber = models.IntegerField(_("Serlial Limit For One Contact Number"))
    patientAccountLimitForOneNumber = models.IntegerField(_("patient Account Limit For One Number"))
    indexingForLateCommer = models.IntegerField(_("Indexing For Late Commer"))
    indexingForReportShower = models.IntegerField(_("Indexing For Report Shower"))
    isSendMessage = models.BooleanField(_("is_send_message"))

class ChemberSchedule(models.Model):
    chember = models.ForeignKey(Chember, related_name="chember_schedule", on_delete=models.CASCADE)
    day = models.CharField(_("Days"), max_length=500)
    startTime = models.TimeField(_("Start Time"), auto_now=False, auto_now_add=False)
    endTime = models.TimeField(_("End Time"), auto_now=False, auto_now_add=False)

