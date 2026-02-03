from flask import Flask, jsonify, request

app = Flask(__name__)

# sample EV dataset (we will upgrade to DB later)
CARS = [
    {"id": 1, "brand": "Tesla", "model": "Model 3", "battery_kwh": 60, "range_km": 491, "price_usd": 38990},
    {"id": 2, "brand": "Nissan", "model": "Leaf", "battery_kwh": 40, "range_km": 270, "price_usd": 28000},
    {"id": 3, "brand": "Hyundai", "model": "Ioniq 5", "battery_kwh": 77.4, "range_km": 507, "price_usd": 41000},
]

@app.route("/")
def home():
    return "EV Hub API running ⚡🚗"

@app.route("/api/cars")
def get_cars():
    return jsonify(CARS)

@app.route("/api/cars/<int:car_id>")
def get_car(car_id):
    car = next((c for c in CARS if c["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(car)

@app.route("/api/range-check")
def range_check():
    car_id = request.args.get("car_id", type=int)
    trip_km = request.args.get("trip_km", type=float)

    car = next((c for c in CARS if c["id"] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    if trip_km is None:
        return jsonify({"error": "trip_km is required"}), 400

    can_make_trip = trip_km <= car["range_km"]

    return jsonify({
        "car": f'{car["brand"]} {car["model"]}',
        "trip_km": trip_km,
        "range_km": car["range_km"],
        "can_make_trip": can_make_trip
    })

if __name__ == "__main__":
    app.run(debug=True)
