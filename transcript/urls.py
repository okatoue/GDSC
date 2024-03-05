from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('index/', views.index_view, name='index'),
]