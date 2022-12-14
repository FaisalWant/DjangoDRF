from django.urls import path 


from .views import (
	
	TagApiDetail, 
	TagApiList,
	StartupApiDetail, 
	StartupApiList, 
	NewsLinkAPIDetail, 
	NewsLinkAPIList,
	
	 )
from rest_framework.routers import SimpleRouter


from .viewsets import TagViewSet,StartupViewSet

api_router= SimpleRouter()
api_router.register("tag", TagViewSet, basename="api-tag") 
api_router.register("startup", StartupViewSet, basename="api-startup") 

api_routes = api_router.urls 





urlpatterns= api_routes + [

path("newslink", NewsLinkAPIList.as_view(), name="api-newslink-list"),

path("newslink/<str:startup_slug>/<str:newslink_slug/", NewsLinkAPIDetail.as_view(), name="api-newslink-detail"),

]
