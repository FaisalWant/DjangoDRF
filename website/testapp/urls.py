from django.urls import path 


# from .views import Pong 

from .views import pong, Status

urlpatterns=[

	# path("ping/", Pong.as_view(), name="ping")
	path("ping/", pong, name="ping"),
	path("status/", Status.as_view(), name="site_status")
	]