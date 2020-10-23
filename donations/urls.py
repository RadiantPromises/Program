from django.urls import path
from . import views
# localhost:8000/donations
urlpatterns = [
    path('', views.index),
    path('phases', views.phases),
    path('stripePayment',views.stripePayment),
    path('stripeTesting',views.stripeTesting),
    path('updatePaymentIntent',views.updatePaymentIntent),
]