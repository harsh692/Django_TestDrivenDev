from django.contrib import admin
from django.urls import path,include
from task import urls
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:pk>/',views.detail,name='detail')
]