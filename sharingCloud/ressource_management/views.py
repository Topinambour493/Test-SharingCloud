from cProfile import label
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Ressource

def form_new_ressource(request):
    template = loader.get_template('ressource_management/form_new_ressource.html')
    return HttpResponse(template.render({}, request))

def add_ressource(request):
    label_ressource=request.POST['label'].strip()
    type_ressource=request.POST['type'].strip()
    localization_ressource=request.POST['localization'].strip()
    people_capacity_ressource=request.POST['people_capacity']
    if 0 in [len(label_ressource),len(type_ressource),len(localization_ressource),len(people_capacity_ressource)]:
        return render(request, 'ressource_management/form_new_ressource.html', {
            'error_message': "Tu n'as pas rempli tous les champs",
        })
    new_ressource = Ressource(label=label_ressource,type=type_ressource,localization=localization_ressource,people_capacity=people_capacity_ressource)
    new_ressource.save()
    return HttpResponseRedirect(reverse("ressource_management:index"))

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
    ressource = get_object_or_404(Ressource, pk=ressource_id)
    return render(request, 'ressource_management/detail.html', {'ressource':ressource})
