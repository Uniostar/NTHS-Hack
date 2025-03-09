from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("data/", views.receive_sensor_data, name="receive_sensor_data")
]