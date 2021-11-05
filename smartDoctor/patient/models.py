from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Patient(models.Model):
    chember = models.ForeignKey("chember.Chember", related_name="chember_patient", on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    contactNumber = models.IntegerField(_("Contact Number"))
    age = models.IntegerField(_("Age"))
    gender = models.CharField(_("Gender"), max_length=50)
    date = models.DateTimeField(_("Date"), auto_now_add=True)
    

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient_prescription', on_delete=models.CASCADE)
    descrioption = models.CharField(_("Drescrioption"), max_length=50)

class MedicineForPrescription(models.Model):
    prescription = models.ForeignKey(Prescription, related_name="prescripton_medicine", on_delete=models.CASCADE)
    medicine = models.ForeignKey("Doctor.LoaclMedicine", related_name="patient_medicine", on_delete=models.CASCADE, null=True)
    howManyDays = models.IntegerField(_("How Many Days"),default=0)
    howManyTimes = models.CharField(_("How Many Days"), max_length=50)

class TestForPrescriotion(models.Model):
    test = models.ForeignKey("Doctor.LocalTest",related_name='patient_text', on_delete=models.CASCADE, null=True)
    prescription = models.ForeignKey(Prescription, related_name="Prescription_text", on_delete=models.CASCADE)
    description = models.TextField(_("Description"))

class History(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient_history', on_delete=models.CASCADE)
    chember = models.ForeignKey('chember.Chember', related_name='chember_patient_history', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="history", on_delete=models.CASCADE)
    log = models.CharField(_("Log"), max_length=500)
    date = models.DateTimeField(_("Date"),  auto_now_add=False)