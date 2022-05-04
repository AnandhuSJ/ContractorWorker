import os
import random
from django.urls import reverse
from django.shortcuts import render, redirect
from job.models import *
from datetime import datetime,date
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django. contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def Login(request):

       User = designation.objects.get(designation="User")
       Worker = designation.objects.get(designation="Worker")
       Contractor = designation.objects.get(designation="Contractor")
       if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'SuperAdmin_index')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=User.id,status="Approval" or "approval").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Usr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Usr_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'User_index.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Worker.id,status="Approval" or "Approval").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Wkr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Wkr_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'WorkerOrContractor_index.html',{'mem1':mem1})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Contractor.id,status="Approval" or "Approval").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Cntr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Cntr_id'] = member.id 
                mem2=user_registration.objects.filter(id= member.id)
                
                return render(request,'WorkerOrContractor_index.html',{'mem2':mem2})        
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
       return render(request,'login.html')



def RegistrationForm(request):
       if request.method == 'POST':
        acc = user_registration()
        acc.fullname = request.POST['username']
        acc.gender = request.POST['gender']
        acc.email = request.POST['email']
        acc.password = request.POST['psswd']
        acc.mobile = request.POST['mobile']
        acc.aadharno = request.POST['aadharno']
        acc.pincode = request.POST['pincode']
        acc.education = request.POST['education']
        acc.idproof = request.FILES['id_proof']
        acc.addressproof = request.FILES['address_proof']
        acc.photo = request.FILES['pic']
        acc.city = request.POST['city']
        acc.country = request.POST['country']
        acc.address1 = request.POST['address1']
        acc.skills = request.POST['skills']
        acc.experience = request.POST['experience']
        acc.joiningdate = datetime.now()
        acc.save()
       return render(request,'RegistrationForm.html')
        
       



def User_index(request):
        
       return render(request, 'User_index.html')

def User_MyProfile(request):
        
       return render(request, 'User_MyProfile.html')

def User_MyRegister(request):
        
       return render(request, 'User_MyRegister.html')

def User_PostFeedback(request):
        
       return render(request, 'User_PostFeedback.html')       

def User_ViewWorkDetails(request):
        
       return render(request, 'User_ViewWorkDetails.html')

def User_WorkerDetails_table(request):
        
       return render(request, 'User_WorkerDetails_table.html')

def User_ContractorDetails_table(request):
        
       return render(request, 'User_ContractorDetails_table.html')



def SuperAdmin_index(request):
        
       return render(request, 'SuperAdmin_index.html')

def SuperAdmin_WorkerWorkDetails_cards(request):
        
       return render(request, 'SuperAdmin_WorkerWorkDetails_cards.html')

def SuperAdmin_ActiveWorkerWorkDetails_table(request):
        
       return render(request, 'SuperAdmin_ActiveWorkerWorkDetails_table.html') 

def SuperAdmin_PreviousWorkerWorkDetails_table(request):
        
       return render(request, 'SuperAdmin_PreviousWorkerWorkDetails_table.html')              


def SuperAdmin_ContractorWorkDetails_cards(request):
        
       return render(request, 'SuperAdmin_ContractorWorkDetails_cards.html')     


def SuperAdmin_ActiveContractorWorkDetails_table(request):
        
       return render(request, 'SuperAdmin_ActiveContractorWorkDetails_table.html')  


def SuperAdmin_PreviousContractorWorkDetails_table(request):
        
       return render(request, 'SuperAdmin_PreviousContractorWorkDetails_table.html')

def SuperAdmin_UserDetails(request):
        
       return render(request, 'SuperAdmin_UserDetails.html')       




def WorkerOrContractor_index(request):
        
       return render(request, 'WorkerOrContractor_index.html')  


def WorkerOrContractor_AddWorkDetails(request):
        
       return render(request, 'WorkerOrContractor_AddWorkDetails.html') 


def WorkerOrContractor_ViewWorkDetails(request):
        
       return render(request, 'WorkerOrContractor_ViewWorkDetails.html') 

def WorkerOrContractor_UpdateWorkDetails(request):
        
       return render(request, 'WorkerOrContractor_UpdateWorkDetails.html')             


def WorkerOrContractor_ViewFeedbackDetails(request):
        
       return render(request, 'WorkerOrContractor_ViewFeedbackDetails.html')     


def WorkerOrContractor_MyProfile(request):
        
       return render(request, 'WorkerOrContractor_MyProfile.html')         







