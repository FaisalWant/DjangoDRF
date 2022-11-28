from django.urls import path 


from .views import (
	TagApiDetail, 
	TagApiList,
	StartupApiDetail, 
	StartupApiList )




urlpatterns=[

path("<str:slug>/", TagApiDetail.as_view(), name="api-tag-detail"),
path("startup/<str:slug>/", StartupApiDetail.as_view(), name="api-startup-detail"),
path("", TagApiList.as_view(), name="api-tag-list"),
path("startup", StartupApiList.as_view(), name="api-startup-list")

]