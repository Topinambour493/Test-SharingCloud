from django.urls import path

from . import views

app_name = 'ressource_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('car', views.car, name='car'),
    path('<int:ressource_id>/', views.detail, name='detail'),
    path('form_new_ressource', views.form_new_ressource, name='form_new_ressource'),
    path('add_ressource', views.add_ressource, name='add_ressource'),
]