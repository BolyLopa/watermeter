# === Stage 4: Редактирование записей ===
# Project: WaterMeter
from datetime import date


ALLOWED_FIELDS = ("name", "location", "rate", "calibration_date")


class WaterMeter:
    def __init__(self, meter_id, name, location, rate, calibration_date):
        self.meter_id = meter_id
        self.name = name
        self.location = location
        self.rate = rate
        self.calibration_date = calibration_date


def update_water_meter(meters, meter_id, changes):
    for meter in meters:
        if meter.meter_id == meter_id:
            for key, value in changes.items():
                if key not in ALLOWED_FIELDS:
                    raise ValueError(f"Поле '{key}' нельзя изменить")
                setattr(meter, key, value)
            return meter
    return None


if __name__ == "__main__":
    meters = [
        WaterMeter(1, "Кухня", "Квартира", 7.5, date(2023, 1, 15)),
    ]
    changes = {"name": "Гостиная", "rate": 8.0}
    updated = update_water_meter(meters, 1, changes)
    print(updated.name, updated.rate)
