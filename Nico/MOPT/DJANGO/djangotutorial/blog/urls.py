
from django.urls import path

from blog import views

urlpatterns = [
    path('holaBlog/', views.hola_món, name='hola_món'),
]
