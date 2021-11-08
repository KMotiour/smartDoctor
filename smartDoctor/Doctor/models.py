from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'doctor/{filename}'.format(filename=filename)


# Create your models here.
class DoctorInfo(models.Model):
    doctorName = models.CharField(_("Doctor Name"), max_length=250)
    doctorTitle = models.TextField(_("Doctor Title"))
    phoneNumber = models.IntegerField(_("Phone Number"))
    speciality = models.CharField(_("Speciality"), max_length=500)
    blog = models.TextField(_("Blog"))
    image = models.FileField(_("Image"), upload_to=upload_to, max_length=100)

class LoaclMedicine(models.Model):
    medicineName = models.CharField(_("Medicine Name"), max_length=500)
    medicineType = models.CharField(_("Medicine Type"), max_length=250)
    companyNem = models.CharField(_("Medicine Name"), max_length=500)

class LocalTest(models.Model):
    testName = models.CharField(_("Test Name"), max_length=500)
    type = models.CharField(_("Type"), max_length=250)
    description = models.TextField(_("Descriptio"))


