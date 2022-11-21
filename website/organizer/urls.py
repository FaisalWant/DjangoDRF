from django.urls import path 


from .views import TagApiDetail, TagApiList 



urlpatterns=[

path("<int:pk>/", TagApiDetail.as_view(), name="hello"),
path("", TagApiList.as_view(), name="hello_world")


]