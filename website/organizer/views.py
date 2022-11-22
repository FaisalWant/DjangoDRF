from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse , Http404

from django.views import View 

import json 
from .models import Tag 




class TagApiDetail(View): 

	def get(self, request, pk ): 
		try:
			tag= Tag.objects.get(pk=pk)
		except Tag.DoesNotExist:
			raise Http404()

		tag_json= json.dumps(
			dict(

			 id=tag.pk,
			 name=tag.name, 
			 slug= tag.slug)
			)
		return HttpResponse(tag_json) 





class TagApiList(View): 

	def get(self, request): 

		tag_list = Tag.objects.all()
		if not tag_list:
			raise Http404()


		tag_json = json.dumps([ dict(id= tag.pk, name= tag.name, slug= tag.slug) for tag in tag_list])

		return HttpResponse(tag_json) 


