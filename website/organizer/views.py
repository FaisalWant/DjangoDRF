from django.shortcuts import render

# Create your views here.




from .models import Tag,Startup

from rest_framework.generics import (
	ListApiView,
	RetrieveAPIView
	)

from rest_framework.renderers import JSONRenderer


from .serializers import TagSerializer, StartupSerializer




class TagApiDetail(RetrieveAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer
	lookup_field="slug" 

	


class TagApiList(ListAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer 



class StartupApiDetail(RetrieveAPIView): 

	queryset= Startup.objects.all()
	serializer_class= StartupSerializer 
	lookup_field= "slug" 



class StartupApiList(ListAPIView): 

	queryset= Startup.objects.all()
	serializers_class= StartupSerializer 
	