from django.contrib import admin
from .models import Chember, ChemberSchedule, Settings
# Register your models here.

admin.site.register(Chember)
admin.site.register(Settings)
admin.site.register(ChemberSchedule)
