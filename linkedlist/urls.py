from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_node, name='add_node'),
    path('delete/', views.delete_node, name='delete_node'),
]
