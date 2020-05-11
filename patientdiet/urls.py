from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_profile/', views.new_profile, name='new_profile'),
    path('health_details', views.health_details, name='health_details'),
    path('diet', views.diet, name='diet'),
]
