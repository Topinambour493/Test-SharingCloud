from cProfile import label
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Ressource

class IndexView(generic.ListView):
    template_name = 'ressource_management/index.html'
    context_object_name = 'latest_ressource_list'
    def get_queryset(self):
        return Ressource.objects.all()

class DetailView(generic.DetailView):
    model = Ressource
    template_name = 'ressource_management/detail.html'

class CreateView(generic.CreateView):
    model = Ressource
    fields = '__all__'

    def get_success_url(self):
        return reverse('ressource_management:index')

class UpdateView(generic.UpdateView):
    model = Ressource
    fields = '__all__'
    template_name = 'ressource_management/detail_update.html'

    def get_success_url(self):
        return reverse('ressource_management:index')

class DeleteView(generic.DeleteView):
    model = Ressource
    success_url = reverse_lazy('ressource_management:index')

