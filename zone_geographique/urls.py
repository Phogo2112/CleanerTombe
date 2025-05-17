from django.urls import path
from .views import zone_geographique

urlpatterns = [
    path('',zone_geographique, name="zone_geographique"),
]