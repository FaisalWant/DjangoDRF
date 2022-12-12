

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



class StartupSerializer(HyperlinkedModelSerializer): 


	tags= TagSerializer(many=True)  

	class Meta: 
		model = Startup 
		fields = "__all__" 
		extra_kwargs ={
		"url": {
		"lookup_field": "slug", 
		"view_name": "api-startup-detail"
		}
		}

	def create(self, validated_data): 
		""" Create Startup and associate Tags"""
		tag_data_list= validated_data.pop("tags") 
		startup= Startup.objects.create(**validated_data) 

		# the code below, where we relate bulk-creates objects, 
		# works only in databases that returns PK after bulk insert, 
		# whihc at the time of writing is only PostgreSQL 

		tag_list= Tag.objects.bulk_create(
			[Tag(**tag_data) for tag_data in tag_data_list ])

		startup.tags.add(*tag_list) 
		return startup 






class NewsLinkSerializer(HyperlinkedModelSerializer): 


	startup= StartupSerializer()

	class Meta: 
		model = NewsLink 
		fields= "__all__"






