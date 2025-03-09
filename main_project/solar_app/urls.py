from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("data/", views.receive_sensor_data, name="receive_sensor_data"),
    path("calc/", views.calc, name="calc")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)