from django.urls import path
from . import views
# localhost:8000/
urlpatterns = [
    path('index', views.index),
    path('',views.home),
    path('about',views.about),
    path('our_target',views.our_target),
    path('events',views.events),
    path('contact',views.contact),
    path('navbar',views.navbar),
]