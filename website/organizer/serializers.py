

from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedModelSerializer
	) 

from .models import NewsLink, Startup, Tag 

class TagSerializer(HyperlinkedModelSerializer): 


	class Meta: 
		model = Tag 
		fields = "__all__" 
		extra_kwargs= {
		"url": {
		"lookup_field": "slug",
		"view_name": "api-tag-detail"
		},
		}



class StartupSerializer(ModelSerializer): 


	tags= TagSerializer(many=True)  

	class Meta: 
		model = Startup 
		fields = "__all__" 




class NewsLinkSerializer(ModelSerializer): 


	startup= StartupSerializer()

	class Meta: 
		model = NewsLink 
		fields= "__all__"






