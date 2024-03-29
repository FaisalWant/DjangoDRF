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


from .serializers import TagSerializer, StartupSerializer, NewsLinkSerializer

from django.views.generic import (
	DetailView, 
	ListView,
	CreateView, 
	DeleteView, 
	UpdateView 
	)

from django.views import View 

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import NewsLink, Startup, Tag

from django.shortcuts import (
	get_object_or_404,
	redirect, 
	render )

from .forms import TagForm
from django.urls import reverse_lazy




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
	paginate_by = 3
	queryset= Tag.objects.all()
	template_name="tag/list.html"

class TagDetail(DetailView): 
	""" Display a single Tag""" 

	queryset= Tag.objects.all()
	template_name= "tag/detail.html"


class TagCreate(CreateView): 
	""" Create new Tags via HTML form""" 

	form_class= TagForm
	model=Tag 
	template_name= "tag/form.html" 
	extra_context = {"update": False }


	

class TagUpdate(UpdateView): 

	form_class= TagForm 
	model= Tag 
	template_name= "tag/form.html" 
	extra_context= {"update" : True } 
	


class TagDelete(DeleteView): 
	""" confirm and delete a Tag via HTML""" 
	model= Tag 
	template_name= "tag/confirm_delete.html" 
	success_url = reverse_lazy("tag_list")

	











# DRF-------------------------------------


class TagApiDetail(RetrieveUpdateDestroyAPIView): 

	queryset= Tag.objects.all()
	serializer_class= TagSerializer
	lookup_field="slug" 




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
	



class NewsLinkAPIDetail(RetrieveAPIView):
    """Return JSON for single NewsLink object"""

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        """Override DRF's generic method

        http://www.cdrf.co/3.7/rest_framework.generics/ListAPIView.html#get_object
        """
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug,
        )
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink


class NewsLinkAPIList(ListAPIView):
    """Return JSON for multiple NewsLink objects"""

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
