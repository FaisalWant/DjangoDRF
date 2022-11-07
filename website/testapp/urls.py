from django.urls import path 


from .views import Pong 


urlpatterns=[

	path("ping/", Pong.as_view(), name="ping")

	]