from django.urls import path, include
from myacc import views

urlpatterns = [
    path('', views.index),
]