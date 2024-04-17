from django.urls import path, include

from . import views
from .views import CustomerListView


app_name = 'customer'
urlpatterns = [
    path("", views.CustomerListView.as_view(), name='index'),
    path("<int:pk>/", views.CustomerDetailView.as_view(), name='index_detail'),
    path("add/", views.add_cart, name='add_cart'),
    path("remove/", views.add_cart, name='remove_cart'),
    path("modify_cart/", views.modify_cart, name='modify_cart'),
    path("MRCreate/", views.MRCreateView.as_view(), name='MRCreate'),
]