# === Stage 6: Связанная сущность ===
# Project: WaterMeter
from datetime import date


class Reading:
    def __init__(self, counter_id, value, meter_date):
        self.counter_id = counter_id
        self.value = value
        self.meter_date = meter_date

    def __str__(self):
        return f"Показание {self.value} от {self.meter_date} для счётчика {self.counter_id}"


def add_reading(counter_id, value, meter_date):
    if counter_id is None:
        raise ValueError("Счётчик не выбран")
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Показание должно быть неотрицательным числом")
    if not isinstance(meter_date, date):
        raise ValueError("Дата поверки должна быть объектом date")
    return Reading(counter_id, value, meter_date)


def add_reading_safe(counter_id, value, meter_date):
    try:
        return add_reading(counter_id, value, meter_date)
    except ValueError as exc:
        print(f"Ошибка добавления показания: {exc}")
        return None


if __name__ == "__main__":
    sample = add_reading_safe("CM-001", 1540.0, date(2024, 1, 15))
    print(sample)
