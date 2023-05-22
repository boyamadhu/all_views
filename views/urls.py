"""views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home.as_view(),name='home'),
    path('list_view/',list_view.as_view(),name='list_view'),
    path('create_view/',create_view.as_view(),name='create_view'),

    re_path('^update(?P<pk>\d+)/',update_view.as_view(),name='update_view'),
    re_path('^delete(?P<pk>\d+)/',delete_view.as_view(),name='delete_view'),


    re_path('(?P<pk>\d+)/',detail_view.as_view(),name='detail_view'),
]
