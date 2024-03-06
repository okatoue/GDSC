from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Assuming you have a home view for the root URL
    path('index/', views.index, name='index'),  # Add this line if not already present
]