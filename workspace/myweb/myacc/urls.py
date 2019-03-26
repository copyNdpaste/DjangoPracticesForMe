from django.urls import path, include
from myacc import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.insert),
#    path('<str:acc_type>/', views.index),
]