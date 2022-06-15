"""emailsenderapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from unicodedata import name
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('Luis/', views.hello_luisgerardo, name='luisgerardo'),
    path('María/', views.hello_maria, name='maria'),
    path('Sombri/', views.hello_sombri, name='sombri'),
    #path('<str:names>/', views.hello),
    path('emails/', views.emails, name='emails'),
    path('add', views.add_emails, name='add')
]
