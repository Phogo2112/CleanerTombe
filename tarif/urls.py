from django.urls import path
from .views import article_tarif, get_tombe_list

urlpatterns = [
    path('', get_tombe_list, name='Tarif'),  # ici
    path('tarif/<str:numero_tarif>/', article_tarif, name='tarif')
]