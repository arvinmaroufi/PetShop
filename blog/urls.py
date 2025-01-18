from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article_search/', views.article_search, name='article_search'),
    re_path(r'category/(?P<slug>[-\w]+)/', views.category_article_list, name='category_article_list'),
    re_path(r'(?P<slug>[-\w]+)/', views.article_detail, name='article_detail'),
]

