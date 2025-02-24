from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.order_list, name='orders'),
    path('order/<str:order_id>/', views.order_detail, name='order_detail'),
    path('profile/<str:username>/', views.edit_profile, name='profile'),
    path('setting/', views.setting, name='setting'),
]
