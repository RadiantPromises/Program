from django.urls import path
from . import views
# localhost:8000/info/
urlpatterns = [
    path('', views.index),
    path('home',views.home),
    path('about',views.about)
]