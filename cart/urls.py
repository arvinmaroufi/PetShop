from django.urls import path
from .views import cart_view, add_to_cart, update_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
]
