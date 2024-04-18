"""
URL configuration for job_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name= 'job_site'

urlpatterns = [

    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('person/', include('person.urls')),
    path('chinese/', include('Chinese.urls')),
    path('customer/', include('customer.urls')),
    path('blog/', include('blog.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('photo/', include('photo.urls')),
    # ------------------------------
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done/',views.UserCreateDoneTV.as_view(), name='register_done'),
    # path('logout/', auth_views.LoginView.as_view(next_page='home'), name='logout'), # 추가
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
