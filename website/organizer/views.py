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



@require_safe 
def tag_list(request): 
	""" Render an HTML template """
	tag_list= Tag.objects.all()
	context= {"tag_list": tag_list}
	
	return render(request, "tag/list.html", context) 



@require_safe 
def tag_detail(request, slug): 
	""" Render an HTML template""" 
	tag= get_object_or_404(Tag, slug=slug) 
	
	context= {"tag": tag} 
	
	return render(request, "tag/detail.html",context) 





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
	