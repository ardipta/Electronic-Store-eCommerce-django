from django.urls import path
from . import views

urlpatterns = [
    path('product/laptop', views.laptop, name='laptop'),
    path('product/desktop', views.desktop, name='desktop'),
]
