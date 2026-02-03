from django.urls import path
from .views import car_list

urlpatterns = [
    path("cars/", car_list, name="car_list"),
]
