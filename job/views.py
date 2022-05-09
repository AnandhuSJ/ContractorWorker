import os
import random
from django.urls import reverse
from django.shortcuts import render, redirect
from job.models import *
from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django. contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def Login(request):

       User = designation.objects.get(designation="User")
       Worker = designation.objects.get(designation="Worker")
       Contractor = designation.objects.get(designation="Contractor")
       if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect('SuperAdmin_index')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=User.id, status="Approval" or "approval").exists():

                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['Usr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Usr_id'] = member.id
                mem = user_registration.objects.filter(id=member.id)

                return render(request, 'User_index.html', {'mem': mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=Worker.id, status="Approval" or "Approval").exists():

                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['Wkr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Wkr_id'] = member.id
                mem1 = user_registration.objects.filter(id=member.id)

                return render(request, 'Worker_index.html', {'mem1': mem1})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation=Contractor.id, status="Approval" or "Approval").exists():

                member = user_registration.objects.get(
                    email=request.POST['email'], password=request.POST['password'])
                request.session['Cntr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Cntr_id'] = member.id
                mem2 = user_registration.objects.filter(id=member.id)

                return render(request, 'Contractor_index.html', {'mem2': mem2})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
       return render(request, 'login.html')


def RegistrationForm(request):
    des = designation.objects.get(designation='Worker')
    if request.method == 'POST':
        acc = user_registration()
        acc.designation = des
        acc.fullname = request.POST['username']
        acc.gender = request.POST['gender']
        acc.email = request.POST['email']
        acc.password = request.POST['psswd']
        acc.mobile = request.POST['mobile']
        acc.aadharno = request.POST['aadharno']
        acc.education = request.POST['education']
        acc.idproof = request.FILES['id_proof']
        acc.addressproof = request.FILES['address_proof']
        acc.photo = request.FILES['pic']
        acc.city = request.POST['city']
        acc.address1 = request.POST['address1']
        acc.skills = request.POST['skills']
        acc.experience = request.POST['experience']
        acc.save()
        msg_success = "Registration successfully Check Your Registered Mail"
        return render(request, 'RegistrationForm.html', {'msg_success': msg_success})
    return render(request, 'RegistrationForm.html')


def RegistrationFormUser(request):
      des = designation.objects.get(designation='User')
      if request.method == 'POST':
        usr = user_registration()
        usr.designation = des
        usr.fullname = request.POST['username']
        usr.password = request.POST['psswd']
        usr.email = request.POST['email']
        usr.mobile = request.POST['mobile']
        usr.aadharno = request.POST['aadharno']
        usr.photo = request.FILES['pic']
        usr.save()
        msg_success = "Registration successfull Check Your Registered Mail"
        return render(request, 'RegistrationFormUser.html', {'msg_success': msg_success})
      return render(request, 'RegistrationFormUser.html')


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

         return render(request, 'SuperAdmin_index.html', {'users': users})
    else:
        return redirect('/')


def SuperAdmin_WorkerWorkDetails_cards(request):
     if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)

         return render(request, 'SuperAdmin_WorkerWorkDetails_cards.html', {'users': users})
     else:
        return redirect('/')


def SuperAdmin_ActiveWorkerWorkDetails_table(request):
     if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
         des = designation.objects.get(designation='Worker')
         AWorker = user_registration.objects.filter(designation_id=des).filter(
             status='approval' or 'Approval').all().order_by('-id')
         return render(request, 'SuperAdmin_ActiveWorkerWorkDetails_table.html', {'users': users, 'AWorker': AWorker, 'des': des})
     else:
        return redirect('/')


def SuperAdmin_ActiveWorkerWorkDetails_save(request, id):

    if request.method == 'POST':
       a = user_registration.objects.get(id=id)
       a.status = request.POST['status']
       a.save()

       return redirect('SuperAdmin_WorkerWorkDetails_cards')


def SuperAdmin_PreviousWorkerWorkDetails_table(request):
     if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
         des = designation.objects.get(designation='Worker')
         PWorker = user_registration.objects.filter(designation_id=des).filter(
             status='reject' or 'Reject').all().order_by('-id')
         return render(request, 'SuperAdmin_PreviousWorkerWorkDetails_table.html', {'users': users, 'PWorker': PWorker, 'des': des})
     else:
        return redirect('/')


def SuperAdmin_ContractorWorkDetails_cards(request):
      if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)

         return render(request, 'SuperAdmin_ContractorWorkDetails_cards.html', {'users': users})
      else:
        return redirect('/')


def SuperAdmin_ActiveContractorWorkDetails_table(request):
      if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
         des = designation.objects.get(designation='Contractor')
         AContractor = user_registration.objects.filter(designation_id=des).filter(
             status='approval' or 'Approval').all().order_by('-id')
         return render(request, 'SuperAdmin_ActiveContractorWorkDetails_table.html', {'users': users, 'AContractor': AContractor, 'des': des})
      else:
        return redirect('/')


def SuperAdmin_ActiveContractWorkDetails_save(request, id):

    if request.method == 'POST':
       a = user_registration.objects.get(id=id)
       a.status = request.POST['status']
       a.save()

       return redirect('SuperAdmin_ContractorWorkDetails_cards')


def SuperAdmin_PreviousContractorWorkDetails_table(request):
      if 'SAdm_id' in request.session:
         if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
         users = User.objects.filter(id=SAdm_id)
         des = designation.objects.get(designation='Contractor')
         PContractor = user_registration.objects.filter(designation_id=des).filter(
             status='reject' or 'Reject').all().order_by('-id')
         return render(request, 'SuperAdmin_PreviousContractorWorkDetails_table.html', {'users': users, 'PContractor': PContractor, 'des': des})
      else:
        return redirect('/')


def SuperAdmin_UserDetails(request):
       if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='User')
        Userdetails = user_registration.objects.filter(
            designation_id=des).all().order_by('-id')
       return render(request, 'SuperAdmin_UserDetails.html', {'users': users, 'Userdetails': Userdetails, 'des': des})


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
        return render(request, 'User_Accsetting.html', {'mem': mem})
    else:
        return redirect('/')


def User_Profile_Imagechange(request, id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'User_Accsetting.html', {'msg_success': msg_success})


def User_Changepwd(request, id):
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
            messages.add_message(request, messages.INFO,
                                 'Current and New password same')
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

         return render(request, 'User_index.html', {'mem': mem})
     else:
        return redirect('/')


def User_MyProfile(request):
      if 'Usr_id' in request.session:
          if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
          else:
            return redirect('/')
          mem = user_registration.objects.filter(id=Usr_id)
          des = designation.objects.get(designation='User')
          Userprofile = user_registration.objects.filter(
              designation_id=des).all()
          return render(request, 'User_MyProfile.html', {'mem': mem, 'Userprofile': Userprofile, 'des': des})
      else:
        return redirect('/')


def User_MyRegister(request):
     if 'Usr_id' in request.session:
        if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Usr_id)
        des = designation.objects.get(designation='Worker')
        myregister = user_registration.objects.filter(
            designation_id=des).filter(status='approval' or 'Approval').all()
        return render(request, 'User_MyRegister.html', {'mem': mem, 'myregister': myregister, 'des': des})
     else:
        return redirect('/')


def User_PostFeedback(request):
    if 'Usr_id' in request.session:
        if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Usr_id)
        if request.method == 'POST':
               feed = user_registration()
               feed.fullname = request.POST['username']
               feed.email = request.POST['email']
               feed.password = request.POST['psswd']
               feed.save()
               msg_success = "Feedback given successfully"
               return render(request, 'User_Accsetting.html', {'msg_success': msg_success})
        return render(request, 'User_Accsetting.html', {'mem': mem})
    else:
        return redirect('/')


def User_ViewWorkDetails_card(request):
    if 'Usr_id' in request.session:
         if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
         else:
            return redirect('/')
         mem = user_registration.objects.filter(id=Usr_id)

         return render(request, 'User_ViewWorkDetails_card.html', {'mem': mem})
    else:
        return redirect('/')


def User_WorkerDetails_table(request):
     if 'Usr_id' in request.session:
         if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
         else:
            return redirect('/')
         mem = user_registration.objects.filter(id=Usr_id)
         des = designation.objects.get(designation='Worker')
         workerdetails = user_registration.objects.filter(
             designation_id=des).filter(status='approval' or 'Approval').all()
         return render(request, 'User_WorkerDetails_table.html', {'mem': mem, 'workerdetails': workerdetails, 'des': des})
     else:
        return redirect('/')


def User_ContractorDetails_table(request):
     if 'Usr_id' in request.session:
         if request.session.has_key('Usr_id'):
            Usr_id = request.session['Usr_id']
         else:
            return redirect('/')
         mem = user_registration.objects.filter(id=Usr_id)
         des = designation.objects.get(designation='Contractor')
         contractordetails = user_registration.objects.filter(
             designation_id=des).filter(status='approval' or 'Approval').all()
         return render(request, 'User_ContractorDetails_table.html', {'mem': mem, 'contractordetails': contractordetails, 'des': des})
     else:
        return redirect('/')


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
        return render(request, 'Worker_Accsetting.html', {'mem1': mem1})
    else:
        return redirect('/')


def Worker_Profile_Imagechange(request, id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Worker_Accsetting.html', {'msg_success': msg_success})


def Worker_Changepwd(request, id):
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
            messages.add_message(request, messages.INFO,
                                 'Current and New password same')
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
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Wkr_id)

        return render(request, 'Worker_index.html', {'mem1': mem1})
    else:
        return redirect('/')


def Worker_AddWorkDetails(request):
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.get(id=Wkr_id)
        return render(request, 'Worker_AddWorkDetails.html', {'mem1': mem1,'Wkr_id': Wkr_id})
    else:
        return redirect('/')


def Worker_AddWorkDetailssave(request, id):
    a = user_registration.objects.get(id=id)
    if request.method == 'POST':
        a.fullname = request.POST['workername']
        a.worktype = request.POST['workertype']
        a.skills = request.POST['skills']
        a.experience = request.POST['experience']
        a.address1 = request.POST['address1']
        a.address2 = request.POST['address2']
        a.cityandpin = request.POST['cityandpin']
        a.mobile = request.POST['mobile']
        a.aadharno = request.POST['aadharno']
        a.costdayshrs = request.POST['costdayshrs']
        a.save()
        msg_success = "Work Details Added successfully"
        return render(request, 'Worker_AddWorkDetails.html',{'msg_success': msg_success,'Wkr_id':id})
    else:
        return render(request, 'Worker_AddWorkDetails.html')
        


def Worker_ViewWorkDetails(request):
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Wkr_id)
        des = designation.objects.get(designation='Worker')
        workerdetails = user_registration.objects.filter(designation_id = des).filter(status='approval' or 'Approval').all().order_by('-id')
        return render(request, 'Worker_ViewWorkDetails.html',{'mem1':mem1,'workerdetails':workerdetails,'des':des})  
    else:
        return redirect('/')
         
        

def Worker_UpdateWorkDetails(request):
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.get(id=Wkr_id)
        return render(request, 'Worker_UpdateWorkDetails.html', {'mem1': mem1,'Wkr_id': Wkr_id})
    else:
        return redirect('/')
         

def Worker_UpdateWorkDetailssave(request, id):
    a = user_registration.objects.get(id=id)
    if request.method == 'POST':
        a.fullname = request.POST['workername']
        a.worktype = request.POST['workertype']
        a.skills = request.POST['skills']
        a.experience = request.POST['experience']
        a.address1 = request.POST['address1']
        a.address2 = request.POST['address2']
        a.cityandpin = request.POST['cityandpin']
        a.mobile = request.POST['mobile']
        a.aadharno = request.POST['aadharno']
        a.costdayshrs = request.POST['costdayshrs']
        a.save()
        msg_success = "Work Details Updated successfully"
        return render(request, 'Worker_ViewWorkDetails.html',{'msg_success': msg_success,'Wkr_id':id})
    else:
        return render(request, 'Worker_UpdateWorkDetails.html')


def Worker_ViewFeedbackDetails(request):
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Wkr_id)
        des = designation.objects.get(designation='Contractor' or 'User')
        workerfeedback = user_registration.objects.filter(designation_id = des).all()
        return render(request, 'Worker_ViewFeedbackDetails.html',{'mem1':mem1,'workerfeedback':workerfeedback})  
    else:
        return redirect('/')
             


def Worker_MyProfile(request):
    if 'Wkr_id' in request.session:
        if request.session.has_key('Wkr_id'):
            Wkr_id = request.session['Wkr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Wkr_id)
        des = designation.objects.get(designation='Worker')
        workerprofile = user_registration.objects.filter(designation_id = des).filter(status='approval' or 'Approval').all()
        return render(request, 'Worker_MyProfile.html',{'mem1':mem1,'workerprofile':workerprofile})  
    else:
        return redirect('/')
         
        

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
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.filter(id=Cntr_id)
        return render(request, 'Contractor_index.html',{'mem2':mem2}) 
    else:
        return redirect('/')

def Contractor_AddWorkDetails(request):
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.get(id=Cntr_id)
        return render(request, 'Contractor_AddWorkDetails.html', {'mem2': mem2,'Cntr_id': Cntr_id})
    else:
        return redirect('/')


def Contractor_AddWorkDetailssave(request,id):
        b = user_registration.objects.get(id=id)
        if request.method == 'POST':
            b = user_registration()
            b.fullname = request.POST['contractorname']
            b.contracttype = request.POST['contractortype']
            b.skills = request.POST['skills']
            b.experience = request.POST['experience']
            b.address1 = request.POST['address1']
            b.address2 = request.POST['address2']
            b.cityandpin = request.POST['cityandpin']
            b.mobile = request.POST['mobile']
            b.aadharno = request.POST['aadharno']
            b.costdayshrs = request.POST['costdayshrs'] 
            b.save()
            msg_success = "Work Details Updated successfully"
            return render(request, 'Contractor_AddWorkDetails.html', {'msg_success': msg_success,'Cntr_id':id})
        else:    
            return render(request, 'Contractor_AddWorkDetails.html') 
       
        
      


def Contractor_ViewWorkDetails(request):
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.filter(id=Cntr_id)
        des = designation.objects.get(designation='Contractor')
        contractordetails = user_registration.objects.filter(designation_id = des).filter(status='approval' or 'Approval').all().order_by('-id')
        return render(request, 'Contractor_ViewWorkDetails.html',{'mem2':mem2,'contractordetails':contractordetails,'des':des}) 
    else:
        return redirect('/')
        

def Contractor_UpdateWorkDetails(request):
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.get(id=Cntr_id)
        return render(request, 'Contractor_UpdateWorkDetails.html', {'mem2': mem2,'Cntr_id': id})
    else:
        return redirect('/')        

def Contractor_UpdateWorkDetailssave(request,id):
        b = user_registration.objects.get(id=id)
        if request.method == 'POST':
            b = user_registration()
            b.fullname = request.POST['contractorname']
            b.contracttype = request.POST['contractortype']
            b.skills = request.POST['skills']
            b.experience = request.POST['experience']
            b.address1 = request.POST['address1']
            b.address2 = request.POST['address2']
            b.cityandpin = request.POST['cityandpin']
            b.mobile = request.POST['mobile']
            b.aadharno = request.POST['aadharno']
            b.costdayshrs = request.POST['costdayshrs'] 
            b.save()
            msg_success = "Work Details Updated successfully"
            return render(request, 'Contractor_ViewWorkDetails.html', {'msg_success': msg_success,'Cntr_id':id})
        else:    
           return render(request, 'Contractor_UpdateWorkDetails.html') 
   

def Contractor_PostFeedbackDetails(request):
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.filter(id=Cntr_id)
        return render(request, 'Contractor_PostFeedbackDetails.html',{'mem2':mem2}) 
    else:
        return redirect('/')
            


def Contractor_MyProfile(request):
    if 'Cntr_id' in request.session:
        if request.session.has_key('Cntr_id'):
            Cntr_id = request.session['Cntr_id']
        else:
            return redirect('/')
        mem2 = user_registration.objects.filter(id=Cntr_id)
        des = designation.objects.get(designation='Contractor')
        contractorprofile = user_registration.objects.filter(designation_id = des).filter(status='approval' or 'Approval').all()
        return render(request, 'Contractor_MyProfile.html',{'mem2':mem2,'contractorprofile':contractorprofile}) 
    else:
        return redirect('/')
        

