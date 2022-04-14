from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car', views.car, name='car'),
    path('<int:ressource_id>/', views.detail, name='detail'),
]