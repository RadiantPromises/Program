from django.urls import path
from . import views
# localhost:8000/communications
urlpatterns = [
    path('', views.index),
    path('twilio',views.texts),
    path('twilio/sendMessage',views.sendMessage), # Careful, Actually sends a message!
]