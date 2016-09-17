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
    data = serializers.serialize("json", [User.objects.get(pk=user_id)]) #creates a json object in data
    return HttpResponse(data)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)