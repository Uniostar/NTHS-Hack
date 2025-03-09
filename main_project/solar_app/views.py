from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData

def home(request):
    return render(request, "solar_app/index.html")

@api_view(["POST"])
def receive_sensor_data(request):
    if request.method == "POST":
        sensor_value = request.data.get("sensor_value")
        if sensor_value:
            SensorData.objects.create(sensor_value=sensor_value)
            return Response({"message": "Data received"}, status=201)
        else:
            return Response({"message": "Failed"}, status=400)