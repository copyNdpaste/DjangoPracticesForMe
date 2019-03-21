from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blog),
    path('write/', views.write),
    path('title/', views.title),
    path('form/', views.inputForm),
]