from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='resume'),
    path('index', views.index, name='index'),
    path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
   ]
