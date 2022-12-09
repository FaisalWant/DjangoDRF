from django.shortcuts import render

# Create your views here.



from django.shortcuts import get_object_or_404


from django.views.decorators.http import require_safe 

from .models import Tag,Startup

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	ListCreateAPIView
	)

from rest_framework.renderers import JSONRenderer


from .serializers import TagSerializer, StartupSerializer

from django.views.generic import DetailView, ListView

from rest_framework.response import Response 

from rest_framework.status import HTTP_204_NO_CONTENT

from rest_framework.status immport(
	RetrieveUpdateAPIView
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


class TagApiDetail(RetrieveUpdateAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer
	lookup_field="slug" 

	def delete(self, request, slug): 
		"""DELETE the Tag with specified slug""" 
		tag= self.get_object()
		tag.delete()
		return Response(status= HTTP_204_NO_CONTENT) 

	


class TagApiList(ListCreateAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer 



class StartupApiDetail(RetrieveAPIView): 

	queryset= Startup.objects.all()
	serializer_class= StartupSerializer 
	lookup_field= "slug" 



class StartupApiList(ListAPIView): 

	queryset= Startup.objects.all()
	serializers_class= StartupSerializer 
	