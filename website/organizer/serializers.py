

from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedModelSerializer,
	HyperlinkedRelatedField,
	SerializerMethodField,

	) 

from .models import NewsLink, Startup, Tag 

from rest_framework.reverse import reverse 

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


	tags= TagSerializer(many=True, read_only=True)  

	class Meta: 
		model = Startup 
		fields = "__all__" 
		extra_kwargs ={
		"url": {
		"lookup_field": "slug", 
		"view_name": "api-startup-detail"
		}
		}








class NewsLinkSerializer(ModelSerializer): 

	url=SerializerMethodField()
	startup= HyperlinkedRelatedField(
		queryset= Startup.objects.all(), 
		lookup_field="slug", 
		view_name="api-startup-detail")

	class Meta: 
		model = NewsLink 
		exclude=("id",) 


	def get_url(self, newslink): 
		""" build full URL for NewsLink API detail""" 

		return reverse("api-newslink-detail",
			kwargs=dict(
				startup_slug= newslink.startup.slug, 
				newslink_slug= newslink.slug, 
				),
			request= self.context["request"],
			)






