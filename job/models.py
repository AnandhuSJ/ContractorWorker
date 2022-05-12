from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class designation(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation




class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)                                                               
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
    # work = models.CharField(max_length=240, null=True, default='')
    skills = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    addressproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    worktype = models.CharField(max_length=100, null=True, default='')
    cityandpin = models.CharField(max_length=100, null=True, default='')
    costdayshrs = models.CharField(max_length=100, null=True, default='')
    usertype = models.CharField(max_length=100,null=True, default='')
    contracttype = models.CharField(max_length=100,null=True, default='')

    def __str__(self):
        return self.fullname

    
class Feedback(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,related_name='Feedbackuser', null=True, blank=True)
    reporterid = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,related_name='Feedbackworkerid', null=True, blank=True)
    feedback = models.CharField(max_length=240, null=True)
