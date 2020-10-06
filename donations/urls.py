from django.urls import path
from . import views
# localhost:8000/donations
urlpatterns = [
    path('', views.index),
    path('stripe',views.stripePayment),
    path('stripeTesting',views.stripeTesting),
]