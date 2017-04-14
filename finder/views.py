	from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from collection.forms import ContactForm



def index(request):
    return render(request, 'finder/index.html')
#    Enter Interests <strong>{{ boldmessage }}</strong><br />


def about(request):
    return HttpResponse("About Page")


def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })
