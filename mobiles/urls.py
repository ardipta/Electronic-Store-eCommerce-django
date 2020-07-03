from django.urls import path
from . import views

urlpatterns = [
    path('product/smartphone', views.smartphone, name='smartphone'),
    path('product/mobilephone', views.mobilephone, name='mobilephone'),
    path('product/tablet', views.tablet, name='tablet'),
]
