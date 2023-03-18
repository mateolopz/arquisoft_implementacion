from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('manejadorhistorias/', views.historias_list, name='historias_list'),
    path('consulta/', views.consulta, name='consulta'),
    path('actualizar/', views.actualizar, name='actualizar'),
]