from ..utils.distance_collector_utils import (collect_city_data_by_name, extract_coords,
                                              get_distance_by_coords, extract_unique)
from ..models import Shipment
from django.utils import timezone
from datetime import timedelta


class ShipmentService:
    price_per_km = 1.2


    @staticmethod
    def collect_city_data(city_from, city_to):
        city_from_data = collect_city_data_by_name(city_from)
        city_to_data = collect_city_data_by_name(city_to)
        return extract_unique(city_from_data), extract_unique(city_to_data)

    @staticmethod
    def get_city_coords(city_data_list, city_index):
        return extract_coords(city_data_list, city_index)

    @staticmethod
    def calculate_distance(origin, destination):
        return get_distance_by_coords(origin, destination)



    @staticmethod
    def create_shipment(**kwargs):
        shipment = Shipment.objects.create(
            title=kwargs.get("title"),
            description=kwargs.get("description"),
            company_id=kwargs.get("company_id"),
            pickup_location_id=kwargs.get("pickup_location_id"),
            delivery_location_id=kwargs.get("delivery_location_id"),
            price=kwargs.get("price"),
            status=kwargs.get("status"),
            created_at=timezone.now(),
            scheduled_at=timezone.now(),
            deadline=timezone.now() + timedelta(days=2),
            dispatcher_id=kwargs.get("dispatcher_id"),
            driver_id=kwargs.get("driver_id"),
            vehicle_id=kwargs.get("vehicle_id"),
            estimated_distance=kwargs.get("distance"),
            notes=kwargs.get("notes")
        )

        return shipment





