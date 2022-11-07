from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.http import require_http_methods 

# Create your views here.


""" views for testapp"""

# from django.views import View 

# class Pong(View): 
# 	""" Respond to ping request""" 

# 	def get(self, request): 
# 		"""" handle get request""" 

# 		return HttpResponse("pong")


""" Function based view"""

@require_http_methods(["GET", "HEAD", "OPTIONS"])

def pong(request): 
	""" Respond to ping"""
	if request.method in ["GET", "HEAD"]: 

		return HttpResponse("pong") 

	else: 
		response= HttpResponse()
		response["Allow"]= ", ".join(['GET' ,'HEAD', 'OPTIONS'])
		return response 