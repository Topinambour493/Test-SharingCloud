from django.urls import path

from . import views

app_name = 'ressource_management'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/read', views.DetailView.as_view(), name='detail'),
    path('add', views.CreateView.as_view(), name='add'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete')
]