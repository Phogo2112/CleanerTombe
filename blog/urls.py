from django.urls import path
from .views import blog, article

urlpatterns =[
    path('', blog, name='Blog'),
    path('article-<str:numero_article>', article, name='blog_article')
]
