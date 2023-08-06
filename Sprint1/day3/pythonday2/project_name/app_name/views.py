from django.shortcuts import render

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def goodbyeworld(request):
    return HttpResponse("Good bye world!")


# Create your views here.
