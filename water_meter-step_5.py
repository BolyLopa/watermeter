# === Stage 5: Удаление и восстановление ===
# Project: WaterMeter
import uuid
from datetime import datetime

class SoftDeleteMixin:
    def __init__(self, id=None):
        self.id = id or uuid.uuid4().hex

    @property
    def is_deleted(self):
        return getattr(self, "_deleted", False)

class WaterMeter(SoftDeleteMixin):
    def __init__(self, name, location, tariff, calibration_date, id=None):
        super().__init__(id)
        self.name = name
        self.location = location
        self.tariff = tariff
        self.calibration_date = calibration_date

    def soft_delete(self):
        self._deleted = True
        return True

    def restore(self):
        self._deleted = False
        return True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "tariff": self.tariff,
            "calibration_date": self.calibration_date,
            "is_deleted": self.is_deleted,
        }

def find_meter(meters, name):
    for meter in meters:
        if not meter.is_deleted and meter.name == name:
            return meter
    return None

def remove_meter(meters, name):
    meter = find_meter(meters, name)
    if meter is None:
        return False
    meter.soft_delete()
    return True

def restore_meter(meters, name):
    meter = find_meter(meters, name)
    if meter is None:
        return False
    meter.restore()
    return True

def list_active_meters(meters):
    return [m for m in meters if not m.is_deleted]

if __name__ == "__main__":
    meters = [
        WaterMeter("Кухня", "Квартира А", 24.5, "2024-01-15"),
        WaterMeter("Санузел", "Квартира Б", 24.5, "2024-02-20"),
    ]

    print("Активные счётчики до удаления:")
    for m in list_active_meters(meters):
        print(f"  {m.name} (место: {m.location})")

    removed = remove_meter(meters, "Кухня")
    print(f"Удаление 'Кухня': {'успешно' if removed else 'не найдено'}")

    print("Активные счётчики после удаления:")
    for m in list_active_meters(meters):
        print(f"  {m.name} (место: {m.location})")

    restored = restore_meter(meters, "Кухня")
    print(f"Восстановление 'Кухня': {'успешно' if restored else 'не найдено'}")

    print("Активные счётчики после восстановления:")
    for m in list_active_meters(meters):
        print(f"  {m.name} (место: {m.location})")

    print(f"Всего записей в хранилище: {len(meters)}")
