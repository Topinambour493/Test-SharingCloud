from cProfile import label
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView , LogoutView 
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("authentication:login")
    template_name = "authentication/register.html"

class LoginView(LoginView):
    template_name = 'authentication/login.html'
