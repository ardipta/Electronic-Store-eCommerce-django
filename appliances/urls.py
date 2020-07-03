from django.urls import path
from . import views

urlpatterns = [
    path('product/television', views.television, name='television'),
    path('product/camera', views.camera, name='camera'),
    path('product/ac', views.ac, name='ac'),
    path('product/grinder', views.grinder, name='grinder'),
]
