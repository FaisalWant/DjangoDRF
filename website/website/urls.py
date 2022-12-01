"""website URL Configuration

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
from django.urls import path, include
from testapp import urls as testapp_urls 
from organizer import urls as organizer_urls

from blog.routers import urlpatterns as blog_urls 
from organizer.routers import urlpatterns as organizer_urls

api_urls = blog_urls + organizer_urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(organizer_urls)),
    path("api/v1/", include(api_urls)),
]
