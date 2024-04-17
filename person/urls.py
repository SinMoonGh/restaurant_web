from django.contrib import admin
from django.urls import path, include
from person import views

app_name = 'person'
urlpatterns = [
    path('', views.JobLV.as_view(), name='index'),
    path('data_write/', views.image_upload_view, name='data_write'),
]

