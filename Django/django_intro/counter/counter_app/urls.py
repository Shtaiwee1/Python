from django.urls import path     
from . import views
urlpatterns = [
    path('destroy_session', views.destroy),
    path('', views.index),
    path('addtwo', views.add),
    path('increment', views.increments),
    path('<x>', views.choose),
    
]