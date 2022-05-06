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
     re_path(r'^RegistrationFormUser$', views.RegistrationFormUser, name='RegistrationFormUser'),
   

   ######## User Module ########
     re_path(r'^User_index$', views.User_index, name='User_index'),
     re_path(r'^User_MyProfile$', views.User_MyProfile, name='User_MyProfile'),
     re_path(r'^User_MyRegister$', views.User_MyRegister, name='User_MyRegister'),
     re_path(r'^User_PostFeedback$', views.User_PostFeedback, name='User_PostFeedback'),
     re_path(r'^User_ViewWorkDetails_card$', views.User_ViewWorkDetails_card, name='User_ViewWorkDetails_card'),
     re_path(r'^User_WorkerDetails_table$', views.User_WorkerDetails_table, name='User_WorkerDetails_table'),
     re_path(r'^User_ContractorDetails_table$', views.User_ContractorDetails_table, name='User_ContractorDetails_table'),
     re_path(r'^User_Accsetting/$',views.User_Accsetting,name='User_Accsetting'),
     re_path(r'^User_Profile_Imagechange/(?P<id>\d+)/$',views.User_Profile_Imagechange,name='User_Profile_Imagechange'),
     re_path(r'^User_Changepwd/(?P<id>\d+)/$',views.User_Changepwd,name='User_Changepwd'),
     re_path(r'^User_logout/$',views.User_logout,name='User_logout'),


     re_path(r'^SuperAdmin_logout/$', views.SuperAdmin_logout, name='SuperAdmin_logout'),
     re_path(r'^SuperAdmin_Accountsett/$',views.SuperAdmin_Accountsett,name='SuperAdmin_Accountsett'),
     re_path(r'^SuperAdmin_index$', views.SuperAdmin_index, name='SuperAdmin_index'),
     re_path(r'^SuperAdmin_WorkerWorkDetails_cards$', views.SuperAdmin_WorkerWorkDetails_cards, name='SuperAdmin_WorkerWorkDetails_cards'),
     re_path(r'^SuperAdmin_ActiveWorkerWorkDetails_table$', views.SuperAdmin_ActiveWorkerWorkDetails_table, name='SuperAdmin_ActiveWorkerWorkDetails_table'),
     re_path(r'^SuperAdmin_PreviousWorkerWorkDetails_table$', views.SuperAdmin_PreviousWorkerWorkDetails_table, name='SuperAdmin_PreviousWorkerWorkDetails_table'),
     re_path(r'^SuperAdmin_ContractorWorkDetails_cards$', views.SuperAdmin_ContractorWorkDetails_cards, name='SuperAdmin_ContractorWorkDetails_cards'),
     re_path(r'^SuperAdmin_ActiveContractorWorkDetails_table$', views.SuperAdmin_ActiveContractorWorkDetails_table, name='SuperAdmin_ActiveContractorWorkDetails_table'),
     re_path(r'^SuperAdmin_PreviousContractorWorkDetails_table$', views.SuperAdmin_PreviousContractorWorkDetails_table, name='SuperAdmin_PreviousContractorWorkDetails_table'),
     re_path(r'^SuperAdmin_UserDetails$', views.SuperAdmin_UserDetails, name='SuperAdmin_UserDetails'),

     
     re_path(r'^Worker_index$', views.Worker_index, name='Worker_index'),
     re_path(r'^Worker_AddWorkDetails$', views.Worker_AddWorkDetails, name='Worker_AddWorkDetails'),
     re_path(r'^Worker_ViewWorkDetails$', views.Worker_ViewWorkDetails, name='Worker_ViewWorkDetails'),
     re_path(r'^Worker_UpdateWorkDetails$', views.Worker_UpdateWorkDetails, name='Worker_UpdateWorkDetails'),
     re_path(r'^Worker_ViewFeedbackDetails$', views.Worker_ViewFeedbackDetails, name='Worker_ViewFeedbackDetails'),
     re_path(r'^Worker_MyProfile$', views.Worker_MyProfile, name='Worker_MyProfile'),
     re_path(r'^Worker_Accsetting/$',views.Worker_Accsetting,name='Worker_Accsetting'),
     re_path(r'^Worker_logout/$', views.Worker_logout, name='Worker_logout'),
     re_path(r'^Worker_Profile_Imagechange/(?P<id>\d+)/$',views.Worker_Profile_Imagechange,name='Worker_Profile_Imagechange'),
     re_path(r'^Worker_Changepwd/(?P<id>\d+)/$',views.Worker_Changepwd,name='Worker_Changepwd'),
    
     re_path(r'^Contractor_index$', views.Contractor_index, name='Contractor_index'),
     re_path(r'^Contractor_AddWorkDetails$', views.Contractor_AddWorkDetails, name='Contractor_AddWorkDetails'),
     re_path(r'^Contractor_ViewWorkDetails$', views.Contractor_ViewWorkDetails, name='Contractor_ViewWorkDetails'),
     re_path(r'^Contractor_UpdateWorkDetails$', views.Contractor_UpdateWorkDetails, name='Contractor_UpdateWorkDetails'),
     re_path(r'^Contractor_PostFeedbackDetails$', views.Contractor_PostFeedbackDetails, name='Contractor_PostFeedbackDetails'),
     re_path(r'^Contractor_MyProfile$', views.Contractor_MyProfile, name='Contractor_MyProfile'),
     re_path(r'^Contractor_Accsetting/$',views.Contractor_Accsetting,name='Contractor_Accsetting'),
     re_path(r'^Contractor_logout/$', views.Contractor_logout, name='Contractor_logout'),
     re_path(r'^Contractor_Profile_Imagechange/(?P<id>\d+)/$',views.Contractor_Profile_Imagechange,name='Contractor_Profile_Imagechange'),
     re_path(r'^Contractor_Changepwd/(?P<id>\d+)/$',views.Contractor_Changepwd,name='Contractor_Changepwd'),
    
    

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)