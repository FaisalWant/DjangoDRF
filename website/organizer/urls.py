
from django.urls import path

from .views import (
	TagDetail, 
	TagList,
	TagCreate,
	TagUpdate,
	TagDelete,
	StartupDetail, 
	StartupList
	 ) 

urlpatterns = [

	path("tag/", TagList.as_view(), name="tag_list"),
	path("tag/<str:slug>/", TagDetail.as_view(), name="tag_detail"),
	path("tag/create/", TagCreate.as_view(), name="tag_create"),
	path("tag/<str:slug>/update/", TagUpdate.as_view(), name="tag_update"),
	path("tag/<str:slug>/delete", TagDelete.as_view(), name="tag_delete"),
	path("startup/", StartupList.as_view(),name="startup_list"),
	path("startup/<str:slug>/", StartupDetail.as_view(), name="startup_detail")
	

]