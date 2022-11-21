from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

from django.views import View 

import json 
from .models import Tag 




class TagApiDetail(View): 

	def get(self, request, pk ): 
		tag= Tag.objects.get(pk= pk)
		tag_json= json.dumps(
			dict(id=tag.pk,
			 name=tag.name, 
			 slug= tag.slug)
			)
		return HttpResponse(tag_json) 





class TagApiList(View): 
	def get(self, request): 
		tag_list = Tag.objects.all()
		tag_json = json.dumps([ dict(id= tag.pk, name= tag.name, slug= tag.slug) for tag in tag_list])

		return HttpResponse(tag_json) 


