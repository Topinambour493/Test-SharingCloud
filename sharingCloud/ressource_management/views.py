from cProfile import label
from urllib import request
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from .models import Ressource


def redirectIndexView(request):
    if request.user.has_perms('admin') == True :
        print("voiture")
        return redirect(reverse('ressource_management:index_admin'))
    print("vélo")
    return redirect(reverse('ressource_management:index'))

class IndexView(LoginRequiredMixin,ListView):
    template_name = 'ressource_management/index.html'
    def get_queryset(self):
        return Ressource.objects.all()

class IndexAdminView(PermissionRequiredMixin,ListView):
    permission_required = 'admin'
    template_name = 'ressource_management/index_admin.html'
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
        return reverse('ressource_management:index_admin')

class UpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'admin'
    model = Ressource
    fields = '__all__'
    template_name = 'ressource_management/detail_update.html'

    def get_success_url(self):
        return reverse('ressource_management:index_admin')

@permission_required('admin',raise_exception=True)
def deleteRessource(request,ressource_id):
    Ressource.objects.filter(pk=ressource_id).delete()
    return redirect(reverse('ressource_management:index_admin'))

