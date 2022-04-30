import os
import requests
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect
from job.models import *
from datetime import datetime,date
from django.shortcuts import render
from django.conf import settings
from django. contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render

# Create your views here.

def Login(request):
        
       return render(request, 'Login.html')

def RegistrationForm(request):
        
       return render(request, 'RegistrationForm.html')       



def User_index(request):
        
       return render(request, 'User_index.html')

def User_MyProfile(request):
        
       return render(request, 'User_MyProfile.html')

def User_MyRegister(request):
        
       return render(request, 'User_MyRegister.html')

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







