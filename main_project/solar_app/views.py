from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData, checkData
import json

every = []

def home(request):
    data = checkData.objects.all().values()


    return render(request, "solar_app/index.html", {
        "data": data
    })

@api_view(["POST"])
def receive_sensor_data(request):
    if request.method == "POST":
        # print("Request: ", request)
        # data = json.loads(request.body.decode("utf-8"))
        # print("Data: ", data)
        # sensor_value = data.get("sensor_value")
        # print("Sensor: ", sensor_value)

        checkData.objects.create(item=str(request))

        return Response({"message": "Data received"}, status=201)
        # if not sensor_value is None:
        #     print("Received: ", sensor_value)
        #     SensorData.objects.create(sensor_value=sensor_value)
        # else:
        #     print("request none")
        #     return Response({"message": "Failed. Received: " + str(sensor_value)}, status=400)