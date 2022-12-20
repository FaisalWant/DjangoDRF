from djago.apps import apps 

from django.core.checks import Tags, Warning, register



@register(Tag.models) 
def check_model_str(app_configs=None, **kwargs): 

	""" Ensuer all models define a __str__ methd""" 
	configs=(
		app_configs
		if app_configs
		else apps.get_app_configs()

		)

	problem_models=[

	model 
	for app in configs 
	if not app.name.startswith("django.contrib")
	for model in app.get_models()
	if "__str__" not in model.__dict__

	]

	return [
	Warning(
		"All Models must have a __str__ method", 
		hint=(
			"see https://docs.djangoproject.com/"),

		obj=model, 
		id="suorganizer.W001", 
		)
	for model in problem_models
	]