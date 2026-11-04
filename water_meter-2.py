# === Stage 2: Проверка полей ===
# Project: WaterMeter
import datetime


def normalize_text(value):
    if value is None:
        return ""
    return str(value).strip()


def normalize_date(value):
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    formats = ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m.%m.%Y")
    for fmt in formats:
        try:
            return datetime.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError("Дата поверки должна быть в формате ГГГГ-ММ-ДД или ДД.ММ.ГГГГ")


def validate_meter_name(name):
    if not name:
        raise ValueError("Название счётчика не может быть пустым")
    if len(name) > 100:
        raise ValueError("Название счётчика не должно превышать 100 символов")
    return normalize_text(name)


def validate_meter_place(place):
    if not place:
        raise ValueError("Место установки счётчика не может быть пустым")
    if len(place) > 100:
        raise ValueError("Место установки счётчика не должно превышать 100 символов")
    return normalize_text(place)


def validate_meter_tariff(tariff):
    if tariff is None:
        raise ValueError("Тариф не может быть пустым")
    normalized = normalize_text(tariff)
    if not normalized.replace(".", "").replace(",", "").isdigit():
        raise ValueError("Тариф должен быть числом")
    return normalized


def validate_meter_calibration_date(calibration_date):
    return validate_date_strict(calibration_date)


def validate_date_strict(value):
    if value is None:
        raise ValueError("Дата поверки обязательна")
    normalized = normalize_date(value)
    if normalized is None:
        raise ValueError("Дата поверки должна быть в формате ГГГГ-ММ-ДД или ДД.ММ.ГГГГ")
    return normalized


def build_meter(name, place, tariff, calibration_date):
    validated = {
        "name": validate_meter_name(name),
        "place": validate_meter_place(place),
        "tariff": validate_meter_tariff(tariff),
        "calibration_date": validate_meter_calibration_date(calibration_date),
    }
    return Meter(validated["name"], validated["place"], validated["tariff"], validated["calibration_date"])


class Meter:
    def __init__(self, name, place, tariff, calibration_date):
        self.name = name
        self.place = place
        self.tariff = tariff
        self.calibration_date = calibration_date

    def __repr__(self):
        return "Meter(name={!r}, place={!r}, tariff={!r}, calibration_date={!r})".format(
            self.name, self.place, self.tariff, self.calibration_date
        )


if __name__ == "__main__":
    try:
        meter = build_meter("Кухня", "2024-05-01", 30.5)
        print(meter)
    except ValueError as error:
        print("Ошибка:", error)
