from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

from django.views import View 

import json 
from .models import Tag 

from django.shortcuts import (
	get_list_or_404, 
	get_object_or_404
	)

from rest_framework.renderers import JSONRenderer

from .serializers import TagSerializer




class TagApiDetail(View): 

	def get(self, request, pk ): 

		tag= get_object_or_404(Tag,pk=pk)
		
		s_tag= TagSerializer(tag) 

		tag_json= JSONRenderer().render(s_tag.data)

		return HttpResponse(tag_json, content_type="application/json") 





class TagApiList(View): 

	def get(self, request): 

		tag_list = get_list_or_404(Tag)

		s_tag= TagSerializer(tag_list, many=True) 

		tag_json = JSONRenderer().render(s_tag.data) 

		return HttpResponse(tag_json,content_type="application/json") 




