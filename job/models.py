from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class designation(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation




class contractor(models.Model):
    contracttype = models.CharField(max_length=100)
    cityandpin = models.CharField(max_length=100)
    costdayshrs = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    contractorfeedback = models.CharField(max_length=240, null=True)
   

    def __str__(self):
        return self.contracttype 

class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)  
    contractor = models.ForeignKey(contractor, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationcontractor', null=True, blank=True)                                                               
    fullname = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    city = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    address1 = models.CharField(max_length=240, null=True)
    address2 = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    aadharno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    education = models.CharField(max_length=240, null=True)
    experience = models.CharField(max_length=240, null=True)
    skills = models.CharField(max_length=240, null=True)
    userfeedback = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    addressproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    worktype = models.CharField(max_length=100)
    cityandpin = models.CharField(max_length=100)
    costdayshrs = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class worker(models.Model):
    contractorfeedback = models.ForeignKey(contractor, on_delete=models.DO_NOTHING,null=True, blank=True)
    userfeedback = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)
   

    def __str__(self):
        return self.worktype        
