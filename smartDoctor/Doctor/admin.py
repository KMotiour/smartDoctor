from django.contrib import admin
from .models import DoctorInfo, LoaclMedicine, LocalTest

# Register your models here.

admin.site.register(DoctorInfo)
admin.site.register(LoaclMedicine)
admin.site.register(LocalTest)