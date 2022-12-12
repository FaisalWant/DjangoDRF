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
apt_router.register("startup", StartupViewSet, base_name="api-startup") 

api_routes = api_router.urls 





urlpatterns= api_routes + [

path("newslink", NewsLinkAPIListList.as_view(), name="api-newslink-list"),

path("newslink/<str:startup_slug>/<str:newslink_slug/", NewsLinkAPIDetail.as_view(), name="api-newslink-detail"),

]