from django.urls import path

from . import views

app_name = 'ressource_management'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index_admin',views.IndexAdminView.as_view(), name='index_admin'),
    path('<int:pk>/read', views.DetailView.as_view(), name='detail'),
    path('add', views.CreateView.as_view(), name='add'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
    path('<int:ressource_id>/delete', views.deleteRessource, name='maxi'),
    path('redirect_index',views.redirectIndexView,name="redirect_index")
]