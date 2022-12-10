from django.urls import path 


from .views import (
	TagApiDetail, 
	TagApiList,
	StartupApiDetail, 
	StartupApiList )


from .viewsets import TagViewSet 


tag_create_list= TagViewSet.as_view(
	{

	"get": "list",
	"post": "create"

	})


tag_retrieve_update_delete = TagViewSet.as_view(
	{
	"get": "retrieve",
	"put": "update",
	"patch": "partial_update",
	"delete": "delete"
	})

urlpatterns=[

path("<str:slug>/", TagApiDetail.as_view(), name="api-tag-detail"),
path("startup/<str:slug>/", StartupApiDetail.as_view(), name="api-startup-detail"),
path("tag/", tag_create_list, name="api-tag-list"),
path("tag/<str:slug>/", tag_retrieve_update_delete, name="api-tag-detail"),
path("startup", StartupApiList.as_view(), name="api-startup-list")

]