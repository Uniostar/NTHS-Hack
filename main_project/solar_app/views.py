from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
import json
import math



def home(request):
    return render(request, "solar_app/index.html", {
        "cost": "--",
        "estGen": "--",
        "sav": "--",
        "co2": "--",
        "trees": "--"
    })

def calc(request):
    if request.method == "GET":
        try: 
            sunlight = int(request.GET.get("sunlight", "0"))
            wattage = int(request.GET.get("wattage", "0"))
        
        except Exception as e:
            return redirect("home")
        if not sunlight or not wattage: return redirect("home")

        costOfPanelRef = 20000
        panelWattageRef = 5000

        cost = wattage * (costOfPanelRef/panelWattageRef)

        estGen = (wattage * sunlight)/1000
        sav = estGen * 0.15
        co2 = estGen * 0.11

        estGen *= 30
        estGen = round(estGen, 2)

        sav = round(sav*365, 2)

        co2 = round(co2*365, 2)

        trees = math.ceil(co2/0.13)


        return render(request, "solar_app/index.html", {
            "cost": cost,
            "estGen": estGen,
            "sav": sav,
            "co2": co2,
            "trees": trees
        })

@api_view(["POST"])
def receive_sensor_data(request):
    if request.method == "POST":
        print("Request: ", request)
        data = json.loads(request.body.decode("utf-8"))
        print("Data: ", data)
        sensor_value = data.get("sensor_value")
        print("Sensor: ", sensor_value)


        if not sensor_value is None:
            print("Received: ", sensor_value)
            SensorData.objects.create(sensor_value=sensor_value)
            return Response({"message": "Data received"}, status=201)
        # else:
            print("request none")
            return Response({"message": "Failed. Received: " + str(sensor_value)}, status=400)