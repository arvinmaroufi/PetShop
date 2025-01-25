from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
]
