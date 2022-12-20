from django.db import models

from django_extensions.db.fields import AutoSlugField 


class Tag(Model): 
	name = CharField(max_length=31, unique=True)  
	slug= AutoSlugField(
		help_text= "A label for URL config", 
		max_length= 31, 
		populate_from=["name"]

		)
# Create your models here.

	class Meta:
		ordering=["name"]



	def __str__(self):
		return self.name 
