from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
from django.core import serializers #for json files
import json

from .models import Job, User

# Create your views here.
def index(request):
    return HttpResponse("Hello Andrew. Congrats, you're making progress! :)")

def getUser(request, user_id):
#    if request.method == 'POST'
        
#    else if request.method == 'GET'
        data = serializers.serialize("json", [User.objects.get(pk=user_id)]) #creates a json object in data
        return HttpResponse(data)

def getAllUsers(request):
    data = serializers.serialize("json", User.objects.all()) #creates a json object in data
    return HttpResponse(data)

def getJob(request):
    data = serializers.serialize("json", [Job.objects.get(pk=job_id)]) #creates a json object in data
    return HttpResponse(data)

def getAllJobs(request):
    data = serializers.serialize("json", Job.objects.all()) #creates a json object in data
    return HttpResponse(data)