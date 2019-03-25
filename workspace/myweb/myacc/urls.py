from django.urls import path, include
from myacc import views

urlpatterns = [
    path('', views.index),
    #path('printing/', views.printing),
    path('<str:acc_type>/', views.index),
]