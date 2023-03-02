from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_members, name='add_members'),
    path('del/', views.del_members, name='del_members'),

]