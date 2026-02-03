from django.shortcuts import render
import requests

FLASK_API = "http://127.0.0.1:5000"

def car_list(request):
    r = requests.get(f"{FLASK_API}/api/cars")
    cars = r.json()

    q = request.GET.get("q", "").lower()
    min_range = request.GET.get("min_range", "")

    if q:
        cars = [
            car for car in cars
            if q in car["brand"].lower() or q in car["model"].lower()
        ]

    if min_range:
        try:
            min_range_val = float(min_range)
            cars = [car for car in cars if car["range_km"] >= min_range_val]
        except ValueError:
            pass

    return render(request, "cars/car_list.html", {
        "cars": cars,
        "q": request.GET.get("q", ""),
        "min_range": min_range
    })



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
