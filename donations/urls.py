from django.urls import path
from . import views
# localhost:8000/donations
urlpatterns = [
    path('', views.index),
    path('stripePayment',views.stripePayment),
    path('stripeTesting',views.stripeTesting),
    path('updatePaymentIntent',views.updatePaymentIntent),
    path('twilio',views.texts),
    path('twilio/sendMessage',views.sendMessage),
]