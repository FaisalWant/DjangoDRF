from django.urls import path 


# from .views import Pong 

from .views import pong 

urlpatterns=[

	# path("ping/", Pong.as_view(), name="ping")
	path("ping/", pong, name="ping")

	]