from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  
from django.contrib.auth.models import Group
from chember.models import Chember




class CustomAccountManager(BaseUserManager):

    def create_superuser(self,email,  password, **othersField):
        othersField.setdefault('is_superuser', True)
        othersField.setdefault('is_staff', True)
        othersField.setdefault('is_active', True)

        if othersField.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if othersField.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(email,  password, **othersField)

    def create_user(self, email,  password, **othersField):
        if not email:
            raise ValueError(_('you must provide an email address'))
        email =  self.normalize_email(email)
        user = self.model(email=email, **othersField)
        user.set_password(password)
        user.save()
        return user

        

# Custom authentication model
class NewUsers(AbstractBaseUser, PermissionsMixin):
    chember = models.ForeignKey(Chember, related_name='user_of_chember', on_delete=models.CASCADE, null=True)
    email = models.EmailField(_("email address"), max_length=254, unique=True)  
    userType = models.CharField(max_length=500, choices=[
                                                        ('Doctor', 'Doctor'),
                                                        ('Assistance', 'Assistance'),
                                                        ('Admin', 'Admin')
                                                        ])
    is_allow_to_save_prescription = models.BooleanField(default=False)
    is_allow_to_schedule_queue = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD='email'

    def __str__(self):
        return str(self.email)
