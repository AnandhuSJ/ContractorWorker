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
                
                return render(request,'Worker_index.html',{'mem1':mem1})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Contractor.id,status="Approval" or "Approval").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Cntr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Cntr_id'] = member.id 
                mem2=user_registration.objects.filter(id= member.id)
                
                return render(request,'Contractor_index.html',{'mem2':mem2})        
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
        acc.save()
        msg_success = "Registration successfully Check Your Registered Mail"
        return render(request,'RegistrationForm.html',{'msg_success': msg_success})
     return render(request,'RegistrationForm.html')


def RegistrationFormUser(request):
      if request.method == 'POST':
        acc = user_registration()
        acc.fullname = request.POST['username']
        acc.email = request.POST['email']
        acc.password = request.POST['psswd']
        acc.mobile = request.POST['mobile']
        acc.aadharno = request.POST['aadharno']
        acc.photo = request.FILES['pic']
        acc.save()
        msg_success = "Registration successfully"
        return render(request,'RegistrationFormUser.html',{'msg_success': msg_success}) 
      return render(request,'RegistrationForm.html')      
        
       
def SuperAdmin_Accountsett(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'SuperAdmin_Accountsett.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'SuperAdmin_Accountsett.html', {'msg_error': msg_error})
        return render(request, 'SuperAdmin_Accountsett.html', {'users': users})
    else:
        return redirect('/')

def SuperAdmin_logout(request):
    request.session.flush()
    return redirect("/")





def SuperAdmin_index(request):
    if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
        
         return render(request, 'SuperAdmin_index.html',{'users':users}) 
    else:
        return redirect('/')

def SuperAdmin_WorkerWorkDetails_cards(request):
     if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
        
         return render(request, 'SuperAdmin_WorkerWorkDetails_cards.html')
     else:
        return redirect('/')

def SuperAdmin_ActiveWorkerWorkDetails_table(request):
     if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
         des = designation.objects.get(designation='Worker')
         Worker = user_registration.objects.filter(designation_id = des).filter(status='approval' or 'Approval').all().order_by('-id')
         return render(request, 'SuperAdmin_ActiveWorkerWorkDetails_table.html',{'users':users,'Worker':Worker}) 
     else:
        return redirect('/')
        
def SuperAdmin_PreviousWorkerWorkDetails_table(request):
       if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        
       return render(request, 'SuperAdmin_PreviousWorkerWorkDetails_table.html')              


def SuperAdmin_ContractorWorkDetails_cards(request):
       if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        
       return render(request, 'SuperAdmin_ContractorWorkDetails_cards.html')     


def SuperAdmin_ActiveContractorWorkDetails_table(request):
       if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        
       return render(request, 'SuperAdmin_ActiveContractorWorkDetails_table.html')  


def SuperAdmin_PreviousContractorWorkDetails_table(request):
       if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        
       return render(request, 'SuperAdmin_PreviousContractorWorkDetails_table.html')

def SuperAdmin_UserDetails(request):
       if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        
       return render(request, 'SuperAdmin_UserDetails.html')       



def User_Accsetting(request):
    if 'Usr_id' in request.session:
        if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Usr_id)
       
        if request.method == 'POST':
               acc = user_registration()
               acc.fullname = request.POST['username']
               acc.email = request.POST['email']
               acc.password = request.POST['psswd']
               acc.mobile = request.POST['mobile']
               acc.aadharno = request.POST['aadharno']
               acc.photo = request.FILES['pic']
               acc.save()
               msg_success = "Accounts changed successfully"
               return render(request, 'User_Accsetting.html', {'msg_success': msg_success})
        return render(request,'User_Accsetting.html',{'mem':mem})
    else:
        return redirect('/')
        


def User_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'User_Accsetting.html', {'msg_success': msg_success})

def User_Changepwd(request,id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'User_Accsetting.html', {'msg_success': msg_success})

        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('User_Accsetting')

def User_logout(request):
    if 'Usr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
            


def User_index(request):
       if 'Usr_id' in request.session:
        if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Usr_id)
        
        return render(request, 'User_index.html',{'mem':mem})

def User_MyProfile(request):
        
       return render(request, 'User_MyProfile.html')

def User_MyRegister(request):
       if 'Usr_id' in request.session:
        if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Usr_id)
        myregister = user_registration.objects.all()
        
       return render(request, 'User_MyRegister.html',{'mem':mem,'myregister':myregister})

def User_PostFeedback(request):
        
       return render(request, 'User_PostFeedback.html')       

def User_ViewWorkDetails(request):
        
       return render(request, 'User_ViewWorkDetails.html')

def User_WorkerDetails_table(request):
        
       return render(request, 'User_WorkerDetails_table.html')

def User_ContractorDetails_table(request):
        
       return render(request, 'User_ContractorDetails_table.html')





def Worker_Accsetting(request):
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Wkr_id)
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
            acc.save()
            msg_success = "Accounts changed successfully"
            return render(request, 'Worker_Accsetting.html', {'msg_success': msg_success})
        return render(request,'Worker_Accsetting.html',{'mem1':mem1})
    else:
        return redirect('/')

def Worker_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Worker_Accsetting.html', {'msg_success': msg_success})

def Worker_Changepwd(request,id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Worker_Accsetting.html', {'msg_success': msg_success})
        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('Worker_Accsetting')
    
def Worker_logout(request):
    if 'Wkr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def Worker_index(request):
        
       return render(request, 'Worker_index.html')  


def Worker_AddWorkDetails(request):
        
       return render(request, 'Worker_AddWorkDetails.html') 


def Worker_ViewWorkDetails(request):
        
       return render(request, 'Worker_ViewWorkDetails.html') 

def Worker_UpdateWorkDetails(request):
        
       return render(request, 'Worker_UpdateWorkDetails.html')             


def Worker_ViewFeedbackDetails(request):
        
       return render(request, 'Worker_ViewFeedbackDetails.html')     


def Worker_MyProfile(request):
        
       return render(request, 'Worker_MyProfile.html')     


def Contractor_Accsetting(request):
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.filter(id=Cntr_id)
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
            acc.save()
            msg_success = "Accounts changed successfully"
            return render(request, 'Contractor_Accsetting.html', {'msg_success': msg_success})
        return render(request,'Contractor_Accsetting.html',{'mem2':mem2})
    else:
        return redirect('/')

def Contractor_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Contractor_Accsetting.html', {'msg_success': msg_success})

def Contractor_Changepwd(request,id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Contractor_Accsetting.html', {'msg_success': msg_success})
        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('Contractor_Accsetting')
    
def Contractor_logout(request):
    if 'Cntr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def Contractor_index(request):
        
       return render(request, 'Contractor_index.html') 


def Contractor_AddWorkDetails(request):
        
       return render(request, 'Contractor_AddWorkDetails.html') 


def Contractor_ViewWorkDetails(request):
        
       return render(request, 'Contractor_ViewWorkDetails.html') 

def Contractor_UpdateWorkDetails(request):
        
       return render(request, 'Contractor_UpdateWorkDetails.html')             


def Contractor_PostFeedbackDetails(request):
        
       return render(request, 'Contractor_PostFeedbackDetails.html')     


def Contractor_MyProfile(request):
        
       return render(request, 'Contractor_MyProfile.html')    

