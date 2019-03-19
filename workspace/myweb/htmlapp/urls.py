from django.urls import path
from htmlapp import views

urlpatterns = [
    path('', views.index),
    path('html2/', views.html2),
]