from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'finder/index.html')

def about(request):
    return HttpResponse("About Page")