from rest_framework.serializers import ModelSerializer 


from .models import Post 


from organizer.serializers import (
	StartupSerializer, 
	TagSerializer)




class PostSerializer(ModelSerializer): 
	tags =TagSerializer(many=True) 
	startup= StartupSerializer(many=True) 

	class Meta: 
		model = Post 
		fields ="__all__"