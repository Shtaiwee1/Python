from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.allshows),
    path('shows/new', views.new_show_form),
    path('shows/new/add', views.addshow),
    path('shows/<int:show_id>', views.showdetails),
    path('shows/<int:show_id>/load', views.edit_show_form),
    path('shows/<int:show_id>/delete', views.delete_show),
    path('shows/<int:show_id>/load/edit', views.editnewshow),]