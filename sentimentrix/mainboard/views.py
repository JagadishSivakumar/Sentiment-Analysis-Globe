from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def load_index_page(request):
	"""
	Renders the main page and sending the required information to the globe page.
	"""
	context = {}
	return render(request,"globe/index.html",context=context)

@csrf_exempt
def get_globe_contents(request):
	"""
	Returns the details for the globe to get the json values
	"""
	context = {}
	context['globe'] = [["1990",[11,79,0.7,10,79,1.3,10,79,1.1,10,79,1.2,10,79,1.4,10,78,1.4,8,78,0.9,9,78,0.8,10,77,1.2]],["1995",[11,79,0.9,10,79,1.2,10,79,1,10,79,1.2,10,79,1.2,10,78,1.3,8,78,0.8,9,78,0.7,10,77,1.1]],["2000",[11,79,1.1,10,79,1,10,79,1.2,10,79,1.8,10,79,1.7,10,78,1.5,8,78,1,9,78,0.9,10,77,1.3]]]
	return JsonResponse(context)
