from cProfile import label
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

from .models import Ressource

class IndexView(LoginRequiredMixin,ListView):
    template_name = 'ressource_management/index.html'
    def get_queryset(self):
        return Ressource.objects.all()

class DetailView(LoginRequiredMixin,DetailView):
    model = Ressource
    template_name = 'ressource_management/detail.html'

class CreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'admin'
    model = Ressource
    fields = '__all__'

    def get_success_url(self):
        return reverse('ressource_management:index')

class UpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'admin'
    model = Ressource
    fields = '__all__'
    template_name = 'ressource_management/detail_update.html'

    def get_success_url(self):
        return reverse('ressource_management:index')

class DeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'admin'
    model = Ressource
    success_url = reverse_lazy('ressource_management:index')

