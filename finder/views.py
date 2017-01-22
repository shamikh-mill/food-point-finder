from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Finder says hey there world!")


def about(request):
    return HttpResponse("About Page")