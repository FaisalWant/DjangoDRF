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
from django.contrib.auth import urls as django_auth_urls
from blog.routers import urlpatterns as blog_api_urls 
from organizer.routers import urlpatterns as organizer_api_urls
from blog import urls as blog_urls
from user import urls as user_urls


root_api_url=[
	path("", RootApiView.as_view(), name="api-root")

	]

api_urls = root_api_url+ blog_api_urls + organizer_api_urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(organizer_urls)),
    path("api/v1/", include(api_urls)),
    path("blog/",include(blog_urls)),
    path("", include(testapp_urls)),
    path(
    "o/",
    include(
        "oauth2_provider.urls",
        namespace="oauth2_provider",
    ),
),
    path("", 
    	include(
    		(user_urls, "auth"), namespace= "auth"),
    	),
    path("", TemplateView.as_view(template_name="root.html"),
    	name="site_root",
    	),

    

]
