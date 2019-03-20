from django.urls import path
from htmlapp import views

urlpatterns = [
    path('', views.html),
    path('html2/', views.html2),
    path('tag/<int:tag_num>/', views.tagExample), #tagExample()의 인자로 tag_num이 쓰임
]