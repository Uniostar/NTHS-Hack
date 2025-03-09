from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
import json

def home(request):
    data = SensorData.objects.all().values()


    return render(request, "solar_app/index.html", {
        "data": data
    })

@api_view(["POST"])
def receive_sensor_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        sensor_value = data.get("sensor_value")
        if not sensor_value is None:
            print("Received: ", sensor_value)
            SensorData.objects.create(sensor_value=sensor_value)
            return Response({"message": "Data received"}, status=201)
        else:
            print("request none")
            return Response({"message": "Failed. Received: "}, status=400)