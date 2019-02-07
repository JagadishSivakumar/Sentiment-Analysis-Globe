# @ts-ignore
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import random

# Create your views here.
def bar(request):
	
	labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
	dataset = random.sample(range(1,30),6)
	labelss = json.dumps(labels)
	
	dictionary = {'labels':labelss,'dataset':dataset}
	
	return render(request,'main/basic.html',dictionary)


def jres(request):
	labels = ["Black", "Blue", "Yellow", "Green", "Purple", "Orange"]
	dataset = [15, 20, 25, 27, 15, 33]
	data = {'labels':labels,'dataset':dataset}
	return JsonResponse(data)




