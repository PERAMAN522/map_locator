from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/',views.user, name='home'),
    path('add/addData', views.addData)
]
