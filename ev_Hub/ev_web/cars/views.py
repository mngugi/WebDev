from django.shortcuts import render
import requests

FLASK_API = "http://127.0.0.1:5000"


def car_list(request):
    r = requests.get(f"{FLASK_API}/api/cars")
    cars = r.json()

    q = request.GET.get("q", "").lower()
    min_range = request.GET.get("min_range", "")

    # Search filter
    if q:
        cars = [
            car for car in cars
            if q in car["brand"].lower() or q in car["model"].lower()
        ]

    # Range filter
    if min_range:
        try:
            min_range_int = int(min_range)
            cars = [car for car in cars if car["range_km"] >= min_range_int]
        except ValueError:
            pass

    return render(request, "cars/car_list.html", {
        "cars": cars,
        "q": request.GET.get("q", ""),
        "min_range": min_range,
    })


def car_detail(request, car_id):
    r = requests.get(f"{FLASK_API}/api/cars/{car_id}")
    car = r.json()

    result = None
    trip_km = request.GET.get("trip_km")

    if trip_km:
        check = requests.get(
            f"{FLASK_API}/api/range-check",
            params={"car_id": car_id, "trip_km": trip_km}
        )
        result = check.json()

    return render(request, "cars/car_details.html", {
        "car": car,
        "result": result
    })


def compare_cars(request):
    r = requests.get(f"{FLASK_API}/api/cars")
    cars = r.json()

    car1_id = request.GET.get("car1")
    car2_id = request.GET.get("car2")
    trip_km = request.GET.get("trip_km")

    car1 = None
    car2 = None
    result1 = None
    result2 = None

    if car1_id:
        car1 = requests.get(f"{FLASK_API}/api/cars/{car1_id}").json()

    if car2_id:
        car2 = requests.get(f"{FLASK_API}/api/cars/{car2_id}").json()

    if trip_km and car1_id:
        check1 = requests.get(
            f"{FLASK_API}/api/range-check",
            params={"car_id": car1_id, "trip_km": trip_km}
        )
        result1 = check1.json()

    if trip_km and car2_id:
        check2 = requests.get(
            f"{FLASK_API}/api/range-check",
            params={"car_id": car2_id, "trip_km": trip_km}
        )
        result2 = check2.json()

    return render(request, "cars/compare.html", {
        "cars": cars,
        "car1": car1,
        "car2": car2,
        "car1_id": car1_id,
        "car2_id": car2_id,
        "trip_km": trip_km,
        "result1": result1,
        "result2": result2,
    })
