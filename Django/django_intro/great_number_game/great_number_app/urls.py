from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.comparison),
    path('destroy_session', views.destroy),
    path('goback', views.goback_function),
    path('leaderboard', views.winners)
    
]