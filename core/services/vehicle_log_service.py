from django.utils import timezone
from ..models import VehicleLog

class VehicleLogService:

    @staticmethod
    def get_state(user):
        vehicle = getattr(user, "vehicles", None)

        if vehicle is None:
            return {
                "has_vehicle": False,
                "vehicle": None,
                "already_logged": None
            }
        today = timezone.localdate()

        already_logged = VehicleLog.objects.filter(
            user=user, return_time__date=today
        ).exists()

        return {
            "has_vehicle": True,
            "vehicle": vehicle,
            "already_logged": already_logged
        }

    @staticmethod
    def create_log(user, mileage):
        state = VehicleLogService.get_state(user)

        if not state["has_vehicle"] or state["already_logged"]:
            return None

        log = VehicleLog.objects.create(
            user=user,
            mileage=mileage,
            vehicle=state["vehicle"],
            return_time=timezone.now()
        )

        return log