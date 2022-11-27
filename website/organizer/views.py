from django.shortcuts import render

# Create your views here.




from .models import Tag 

from django.shortcuts import (
	get_list_or_404, 
	get_object_or_404
	)

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response 
from rest_framework.views import APIView 

from .serializers import TagSerializer




class TagApiDetail(APIView): 

	def get(self, request, slug ): 

		tag= get_object_or_404(Tag,slug=slug)
		
		s_tag= TagSerializer(tag, 
			context= {"request": request},

			) 


		
		return Response(s_tag.data) 





class TagApiList(APIView): 

	def get(self, request): 

		tag_list = get_list_or_404(Tag)

		s_tag= TagSerializer(tag_list, 
			many=True,
			context= {"request":request}) 

		

		return Response(s_tag.data)




