"""" Forms for the organizer app"""


from django.forms impor CharField, Form, SlugField 
from django.core.exceptions import ValidationError 


from .models import Tag 

class TagForm(Form): 
	""" HTML form for Tag objects""" 

	name= CharField(max_length=31) 
	slug= SlugField(
		help_text="A label for Url Config", 
		max_length=31, 
		required= False, 
		)


	def clean_name(self): 
		return self.cleaned_data['name'].lower() 


	def clean)slug(self): 
		slug= self.cleaned_data["slug"] 
		if slug= "create":
			raise ValidationError("Slug may not be 'create'")

		return slug 

	def save(self): 
		""" Save the data in the bound form""" 
		return Tag.objects.create(
			name= self.cleaned_data["name"], 
			slug= self.cleaned_data["slug"],
			)
