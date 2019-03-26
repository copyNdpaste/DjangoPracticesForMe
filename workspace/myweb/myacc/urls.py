from django.urls import path, include
from myacc import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.insert),
    path('view/', views.view),
    path('update/', views.update),
    path('delete/', views.delete),
#    path('<str:acc_type>/', views.index),
]