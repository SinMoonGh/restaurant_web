from django.urls import path, include
from . import views

app_name = 'Chinese'
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:pk>/", views.index_detail, name='index_detail'),
    path("<int:pk>/del/", views.index_delete, name='index_delete'),
    path("name/", views.get_name, name='name'),

]