from django.contrib import admin
from django.urls import path, include
from eventos import views

#url de eventos
urlpatterns = [
    path('consultareventos/', views.consultareventos, name="consultareventos"),
    path('creareventos/', views.creareventos, name="creareventos"),
    path('modificareventos/<int:pk>', views.modificareventos, name="modificareventos"),
    path('eliminareventos/<int:pk>', views.eliminareventos, name="eliminareventos"),
]
