"""
URL configuration for DocBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import index, acceuil


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index-du-site"),
    path('tarif/', include('tarif.urls'), name="chemin-pour-page-tarif" ),
    path('blog/', include('blog.urls'), name='chemin_vers_le_blog'),
    path('contact/',include('contact.urls'), name='chemin_vers_contact'),
    path('mention_legal',include('mention_legal.urls'), name='mention_legal'),
    path('zone_geographique/',include('zone_geographique.urls'), name="zone_geographique"),
]


