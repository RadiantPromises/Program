from django.urls import path
from . import views
# localhost:8000/donations
urlpatterns = [
    path('', views.index),
    path('addToCart',views.addToCart),
    path('removeFromCart/<int:cost_id>',views.removeFromCart),
    path('emptyCart',views.emptyCart),
    path('cart',views.cart),
]