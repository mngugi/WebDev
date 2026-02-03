from django.shortcuts import render
import requests

FLASK_API = "http://127.0.0.1:5000"

def car_list(request):
    r = requests.get(f"{FLASK_API}/api/cars")
    cars = r.json()
    return render(request, "cars/car_list.html", {"cars": cars})


def car_detail(request, car_id):
    # get car details
    r = requests.get(f"{FLASK_API}/api/cars/{car_id}")
    car = r.json()

    result = None
    trip_km = request.GET.get("trip_km")

    if trip_km:
        # call flask range check endpoint
        check = requests.get(
            f"{FLASK_API}/api/range-check",
            params={"car_id": car_id, "trip_km": trip_km}
        )
        result = check.json()

    return render(request, "cars/car_detail.html", {"car": car, "result": result})
