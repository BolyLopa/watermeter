# === Stage 7: Связи между сущностями ===
# Project: WaterMeter
from datetime import date


class WaterMeterError(Exception):
    pass


class Reading:
    def __init__(self, counter_id, reading, read_date):
        self.counter_id = counter_id
        self.reading = reading
        self.read_date = read_date

    def __repr__(self):
        return f"Reading(counter_id={self.counter_id}, reading={self.reading}, read_date={self.read_date})"


class WaterMeter:
    def __init__(self, name, place, tariff, calibration_date):
        self.name = name
        self.place = place
        self.tariff = tariff
        self.calibration_date = calibration_date
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def get_readings_for_counter(self, counter_id):
        return [r for r in self.readings if r.counter_id == counter_id]

    def check_integrity(self, counter_id):
        readings = self.get_readings_for_counter(counter_id)
        if not readings:
            raise WaterMeterError(f"Счётчик {counter_id} не имеет показаний")
        for i in range(1, len(readings)):
            prev = readings[i - 1]
            curr = readings[i]
            if curr.reading < prev.reading:
                raise WaterMeterError(f"Показание {curr.reading} меньше предыдущего {prev.reading}")
            if curr.read_date < prev.read_date:
                raise WaterMeterError(f"Дата показания {curr.read_date} раньше предыдущей {prev.read_date}")
        return readings


if __name__ == "__main__":
    meter = WaterMeter("Домашний", "Кухня", 25.5, date(2023, 1, 1))
    meter.add_reading(Reading(1, 100.0, date(2023, 1, 15)))
    meter.add_reading(Reading(1, 150.0, date(2023, 2, 15)))
    meter.add_reading(Reading(1, 200.0, date(2023, 3, 15)))
    print(meter.check_integrity(1))
