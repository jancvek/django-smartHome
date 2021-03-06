"""myproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from boards import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.input, name='input'),
    path('checkConn/', views.checkConn, name='checkConn'),
    path('admin/', admin.site.urls),
    path('temp/', RedirectView.as_view(url='smasa/', permanent=False)),
    re_path(r'^temp/(?P<place>[-\w]+)/$', views.roomTemp, name='roomTemp'),
    path('control/', views.control, name='control'),
    path('ajax/test/', views.ajaxTest, name='ajaxTest'),
    path('farm/', views.farmList, name='farmList'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #for image path purposes
