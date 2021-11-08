from django.db import models
from django.db.models.fields import TimeField
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save,  post_delete, m2m_changed
from django.dispatch import receiver

# Create your models here.
class Chember(models.Model):
    chamber_name = models.CharField(max_length=500)
    location = models.CharField(max_length=1000, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self) -> str:
        return str(self.chamber_name)


class Settings(models.Model):
    chember = models.OneToOneField(Chember, related_name="chember_settings", on_delete=models.CASCADE)
    patinetLimit = models.IntegerField(_("Patient Limit"), default=0)
    SerialLimitForOneContactNumber = models.IntegerField(_("Serlial Limit For One Contact Number"), default=0)
    patientAccountLimitForOneNumber = models.IntegerField(_("patient Account Limit For One Number"), default=0)
    indexingForLateCommer = models.IntegerField(_("Indexing For Late Commer"), default=0)
    indexingForReportShower = models.IntegerField(_("Indexing For Report Shower"), default=0)
    isSendMessage = models.BooleanField(_("is_send_message"), default=False)

    def __str__(self) -> str:
        return str(self.chember.chamber_name)


class ChemberSchedule(models.Model):
    chember = models.ForeignKey(Chember, related_name="chember_schedule", on_delete=models.CASCADE)
    day = models.CharField(_("Days"), max_length=500, null=True)
    startTime = models.TimeField(_("Start Time"), auto_now=False, auto_now_add=False, null=True)
    endTime = models.TimeField(_("End Time"), auto_now=False, auto_now_add=False, null=True)
    
    def __str__(self) -> str:
        return str(self.chember.chamber_name)

@receiver(post_save, sender=Chember)
def create_UserFollow(sender, instance, created, **kwargs):
    if created:
        Settings.objects.create(chember=instance)
        ChemberSchedule.objects.create(chember=instance)
