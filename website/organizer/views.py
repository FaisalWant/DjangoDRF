from django.shortcuts import render

# Create your views here.



from django.shortcuts import get_object_or_404


from django.views.decorators.http import require_safe 

from .models import Tag,Startup

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView
	)

from rest_framework.renderers import JSONRenderer


from .serializers import TagSerializer, StartupSerializer

from django.views.generic import DetailView, ListView


from rest_framework.response import Response 
from rest_framework.status import (
	HTTP_201_CREATED, 
	HTTP_400_BAD_REQUEST,
	)


class StartupList(ListView): 
	""" Display a list of Startups""" 
	queryset= Startup.objects.all()
	template_name= "startup/list.html" 

class StartupDetail(DetailView): 
	""" Display a single Startup """ 
	queryset= Startup.objects.all() 
	template_name= "startup/detail.html" 


class TagList(ListView): 
	""" Display a list of Tags""" 
	queryset= Tag.objects.all()
	template_name="tag/list.html"

class TagDetail(DetailView): 
	""" Display a single Tag""" 

	queryset= Tag.objects.all()
	template_name= "tag/detail.html"




# DRF-------------------------------------


class TagApiDetail(RetrieveAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer
	lookup_field="slug" 

	


class TagApiList(ListAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer 

	def post(self, request): 
		""" Create new Tag upon POST""" 

		s_tag= TagSerializer(
			data=request.data, context={"request": request})

		if s_tag.is_valid(): 
			s_tag.save()
			return Response(
				s_tag.data, status=HTTP_201_CREATED
				)

		return Response(
			s_tag.errors, status=HTTP_400_BAD_REQUEST
			)



class StartupApiDetail(RetrieveAPIView): 

	queryset= Startup.objects.all()
	serializer_class= StartupSerializer 
	lookup_field= "slug" 



class StartupApiList(ListAPIView): 

	queryset= Startup.objects.all()
	serializers_class= StartupSerializer 
	