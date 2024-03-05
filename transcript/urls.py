from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', index_view, name='index'),
]