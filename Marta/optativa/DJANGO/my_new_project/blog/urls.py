from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.hola_mon, name='hola_mon'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
]
