from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.home2, name="home2"),
]
