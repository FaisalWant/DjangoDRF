from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.template import loader
from django.views.decorators.http import require_safe 

from .models import Tag,Startup

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView
	)

from rest_framework.renderers import JSONRenderer


from .serializers import TagSerializer, StartupSerializer



@require_safe 
def tag_list(request): 
	""" Render an HTML template """
	tag_list= Tag.objects.all()
	template= loader.get_template("tag/list.html") 
	context= {"tag_list": tag_list}
	html_context= template.render(context) 
	return HttpResponse(html_content) 



@require_safe 
def tag_detail(request, slug): 
	""" Render an HTML template""" 
	tag= get_object_or_404(Tag, slug=slug) 
	template= loader.get_template("tag/detail.html") 
	context= {"tag": tag} 
	html_content= template.render(context) 
	return HttpResponse(html_content) 





# DRF-------------------------------------


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
	