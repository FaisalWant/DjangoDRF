from django.urls import path 


from .views import (
	
	TagApiDetail, 
	TagApiList,
	StartupApiDetail, 
	StartupApiList 
	NewsLinkAPIDetail, 
	NewsLinkAPIList
	 )


from .viewsets import TagViewSet 

api_router= SimpleRouter()
api_router.register("tag", TagViewSet, base_name="api-tag") 
api_routes = api_router.urls 





urlpatterns= api_routes+ [

path("<str:slug>/", TagApiDetail.as_view(), name="api-tag-detail"),
path("startup/<str:slug>/", StartupApiDetail.as_view(), name="api-startup-detail"),
path("tag/", tag_create_list, name="api-tag-list"),
path("tag/<str:slug>/", tag_retrieve_update_delete, name="api-tag-detail"),
path("startup", StartupApiList.as_view(), name="api-startup-list")

]