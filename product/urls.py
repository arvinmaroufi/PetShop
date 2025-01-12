from django.urls import path, re_path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_search/', views.product_search, name='product_search'),
    re_path(r'category/(?P<slug>[-\w]+)/', views.category_product_list, name='category_product_list'),
    re_path(r'(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]
