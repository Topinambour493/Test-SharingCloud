from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Ressource



def index(request):
    latest_ressource_list = Ressource.objects.all()
    template = loader.get_template('ressource_management/index.html')
    context = {
        'latest_ressource_list': latest_ressource_list,
    }
    return HttpResponse(template.render(context, request))

def car(request):
    return HttpResponse("Hello car.")

def detail(request, ressource_id):
    return HttpResponse("You're looking at ressource %s." % ressource_id)