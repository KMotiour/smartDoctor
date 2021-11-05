from django.contrib import admin
from .models import Patient, Prescription, MedicineForPrescription, TestForPrescriotion, History
# Register your models here.
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(MedicineForPrescription)
admin.site.register(TestForPrescriotion)
admin.site.register(History)