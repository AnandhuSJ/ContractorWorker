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

def login(request):
        
       return render(request, 'login.html')

def User_index(request):
        
       return render(request, 'User_index.html')


def User_RegistrationForm(request):
        
       return render(request, 'User_RegistrationForm.html')