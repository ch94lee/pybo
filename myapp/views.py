
from django.shortcuts import render, HttpResponse
import random
# Create your views here.

def index(request):
    return HttpResponse('Welcome!!'+str(random.random()))

def create(request):
    return HttpResponse('create!!')

def read(request, id):
    return HttpResponse('read!!'+id)