from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


""" views for testapp"""

from django.views import View 

class Pong(View): 
	""" Respond to ping request""" 

	def get(self, request): 
		"""" handle get request""" 

		return HttpResponse("pong")