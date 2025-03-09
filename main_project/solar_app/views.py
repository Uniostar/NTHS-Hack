from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData

def home(request):
    data = SensorData.objects.all().values()


    return render(request, "solar_app/index.html", {
        "data": data
    })

@api_view(["POST"])
def receive_sensor_data(request):
    if request.method == "POST":
        sensor_value = request.data.get("sensor_value").decode("utf-8")
        if not sensor_value is None:
            SensorData.objects.create(sensor_value=sensor_value)
            return Response({"message": "Data received"}, status=201)
        else:
            return Response({"message": "Failed"}, status=400)