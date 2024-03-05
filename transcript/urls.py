from django.urls import path
from .views import index_view

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', index_view, name='index'),
]