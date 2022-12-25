"""" Forms for the organizer app"""


from django.forms import CharField, Form, SlugField 
from django.core.exceptions import ValidationError 


from .models import Tag, Startup

from django.forms import ModelForm

class LowercaseNameMixin: 
	def clean_name(self): 
		return self.cleaned_data["name"].lower() 

class SlugCleanMixin: 
	def clean_slug(self): 

		slug= self.cleaned_data['slug'] 
		if slug == "create":
			raise ValidationError(
				"Slug may not be 'create'."
				)

		return 


class TagForm(LowercaseNameMixin, ModelForm): 
	""" HTML form for Tag objects""" 

	class Meta: 
		model= Tag 
		fields = "__all__"


	
class StartupForm(LowercaseNameMixin, SlugCleanMixin, ModelForm): 
	class Meta:
		model= Startup 
		fields= "__all__" 
