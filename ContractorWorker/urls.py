"""ContractorWorker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from job import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path



urlpatterns = [
    re_path('admin/', admin.site.urls),
     re_path(r'^$', views.Login, name='Login'),
     re_path(r'^RegistrationForm$', views.RegistrationForm, name='RegistrationForm'),
   

   ######## User Module ########
     re_path(r'^User_index$', views.User_index, name='User_index'),
     re_path(r'^User_MyProfile$', views.User_MyProfile, name='User_MyProfile'),
     re_path(r'^User_MyRegister$', views.User_MyRegister, name='User_MyRegister'),
     re_path(r'^User_PostFeedback$', views.User_PostFeedback, name='User_PostFeedback'),
     re_path(r'^User_ViewWorkDetails$', views.User_ViewWorkDetails, name='User_ViewWorkDetails'),
     re_path(r'^User_WorkerDetails_table$', views.User_WorkerDetails_table, name='User_WorkerDetails_table'),
     re_path(r'^User_ContractorDetails_table$', views.User_ContractorDetails_table, name='User_ContractorDetails_table'),


     re_path(r'^SuperAdmin_index$', views.SuperAdmin_index, name='SuperAdmin_index'),
     re_path(r'^SuperAdmin_WorkerWorkDetails_cards$', views.SuperAdmin_WorkerWorkDetails_cards, name='SuperAdmin_WorkerWorkDetails_cards'),
     re_path(r'^SuperAdmin_ActiveWorkerWorkDetails_table$', views.SuperAdmin_ActiveWorkerWorkDetails_table, name='SuperAdmin_ActiveWorkerWorkDetails_table'),
     re_path(r'^SuperAdmin_PreviousWorkerWorkDetails_table$', views.SuperAdmin_PreviousWorkerWorkDetails_table, name='SuperAdmin_PreviousWorkerWorkDetails_table'),
     re_path(r'^SuperAdmin_ContractorWorkDetails_cards$', views.SuperAdmin_ContractorWorkDetails_cards, name='SuperAdmin_ContractorWorkDetails_cards'),
     re_path(r'^SuperAdmin_ActiveContractorWorkDetails_table$', views.SuperAdmin_ActiveContractorWorkDetails_table, name='SuperAdmin_ActiveContractorWorkDetails_table'),
     re_path(r'^SuperAdmin_PreviousContractorWorkDetails_table$', views.SuperAdmin_PreviousContractorWorkDetails_table, name='SuperAdmin_PreviousContractorWorkDetails_table'),
     re_path(r'^SuperAdmin_UserDetails$', views.SuperAdmin_UserDetails, name='SuperAdmin_UserDetails'),


     re_path(r'^WorkerOrContractor_index$', views.WorkerOrContractor_index, name='WorkerOrContractor_index'),
     re_path(r'^WorkerOrContractor_AddWorkDetails$', views.WorkerOrContractor_AddWorkDetails, name='WorkerOrContractor_AddWorkDetails'),
     re_path(r'^WorkerOrContractor_ViewWorkDetails$', views.WorkerOrContractor_ViewWorkDetails, name='WorkerOrContractor_ViewWorkDetails'),
     re_path(r'^WorkerOrContractor_UpdateWorkDetails$', views.WorkerOrContractor_UpdateWorkDetails, name='WorkerOrContractor_UpdateWorkDetails'),
     re_path(r'^WorkerOrContractor_ViewFeedbackDetails$', views.WorkerOrContractor_ViewFeedbackDetails, name='WorkerOrContractor_ViewFeedbackDetails'),
     re_path(r'^WorkerOrContractor_MyProfile$', views.WorkerOrContractor_MyProfile, name='WorkerOrContractor_MyProfile'),
    
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)