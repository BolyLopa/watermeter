# === Stage 3: Хранилище в памяти ===
# Project: WaterMeter
memory_store.py

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class WaterMeter:
    id: str
    name: str
    location: str
    tariff: float
    calibration_date: str


class MemoryStore:
    def __init__(self):
        self._meters: Dict[str, WaterMeter] = {}

    def add_meter(self, name: str, location: str, tariff: float,
                  calibration_date: str) -> WaterMeter:
        meter = WaterMeter(id="", name=name, location=location,
                           tariff=tariff, calibration_date=calibration_date)
        self._meters[meter.id] = meter
        return meter

    def get_meter(self, meter_id: str) -> Optional[WaterMeter]:
        return self._meters.get(meter_id)

    def list_meters(self) -> List[WaterMeter]:
        return list(self._meters.values())


def generate_meter_id(store: MemoryStore) -> str:
    while True:
        candidate = str(len(store._meters) + 1)
        if candidate not in store._meters:
            store._meters[candidate] = None
            return candidate


if __name__ == "__main__":
    store = MemoryStore()
    store.add_meter("Kitchen", "House A", 25.0, "2024-01-15")
    store.add_meter("Garden", "House B", 18.5, "2024-02-20")

    print("All meters:")
    for meter in store.list_meters():
        print(f"  {meter.name} | {meter.location} | "
              f"tariff={meter.tariff} | "
              f"calibration={meter.calibration_date}")

    print("\nRetrieving meter '1':")
    retrieved = store.get_meter("1")
    if retrieved:
        print(f"  Found: {retrieved.name} at {retrieved.location}")
    else:
        print("  Not found")

    print("\nRetrieving meter '999':")
    missing = store.get_meter("999")
    if missing:
        print(f"  Found: {missing.name}")
    else:
        print("  Not found (as expected)")
