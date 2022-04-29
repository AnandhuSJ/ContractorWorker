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
     re_path(r'^User_ViewWorkDetails$', views.User_ViewWorkDetails, name='User_ViewWorkDetails'),
     re_path(r'^User_WorkerDetails_cards$', views.User_WorkerDetails_cards, name='User_WorkerDetails_cards'),
     re_path(r'^User_ActiveWorkerDetails_table$', views.User_ActiveWorkerDetails_table, name='User_ActiveWorkerDetails_table'),
     re_path(r'^User_PreviousWorkerDetails_table$', views.User_PreviousWorkerDetails_table, name='User_PreviousWorkerDetails_table'),
     re_path(r'^User_ContractorDetails_cards$', views.User_ContractorDetails_cards, name='User_ContractorDetails_cards'),
     re_path(r'^User_ActiveContractorDetails_table$', views.User_ActiveContractorDetails_table, name='User_ActiveContractorDetails_table'),
     re_path(r'^User_PreviousContractorDetails_table$', views.User_PreviousContractorDetails_table, name='User_PreviousContractorDetails_table'),
    
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)