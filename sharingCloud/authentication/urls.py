from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('sign_up',views.SignUp.as_view(),name='sign_up'),
    path('logout',views.LogoutView.as_view(),name='logout')
]