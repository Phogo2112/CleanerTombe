from django.urls import path
from .views import mention_legal

urlpatterns = [
    path('', mention_legal, name='mention'),
]
