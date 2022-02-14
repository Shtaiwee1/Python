from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('newdojo', views.create),
    path('newninja', views.addninja),
    path('delete', views.destroy)]