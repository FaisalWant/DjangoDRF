from django.db import models

from django_extensions.db.fields import AutoSlugField 


class Tag(Model): 
	name = CharField(max_length=31) 
	slug= AutoSlugField(
		help_text= "A label for URL config", 
		max_length= 31, 
		populate_from=["name"]

		)
# Create your models here.
