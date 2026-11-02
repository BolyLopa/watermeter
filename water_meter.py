# === Stage 1: Каркас модуля ===
# Project: WaterMeter
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Counter:
    name: str
    location: str
    tariff: float
    calibration_date: date

    def __post_init__(self):
        if self.tariff <= 0:
            raise ValueError("Тариф должен быть положительным")


def make_sample_counters():
    return [
        Counter("Кухня", "Квартира 12", 35.0, date(2023, 6, 1)),
        Counter("Ванная", "Квартира 12", 35.0, date(2023, 6, 1)),
        Counter("Прихожая", "Квартира 12", 35.0, date(2023, 6, 1)),
    ]


def main():
    counters = make_sample_counters()
    for counter in counters:
        print(
            f"Счётчик: {counter.name} | "
            f"Место: {counter.location} | "
            f"Тариф: {counter.tariff} руб/м3 | "
            f"Поверка: {counter.calibration_date}"
        )


if __name__ == "__main__":
    main()
