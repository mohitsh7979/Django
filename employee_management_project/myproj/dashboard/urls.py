from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [

    path('search/', views.search)

]
