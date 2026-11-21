# === Stage 9: Фильтрация записей ===
# Project: WaterMeter
from datetime import date


def filter_by_place_and_range(
    counters, place=None, start=None, end=None
):
    result = []
    for counter in counters:
        if place is not None and counter.get("место") != place:
            continue
        if start is not None and counter.get("дата поверки") < start:
            continue
        if end is not None and counter.get("дата поверки") > end:
            continue
        result.append(counter)
    return result


def compare_months(counters, month1=None, month2=None):
    month1_total = 0.0
    month2_total = 0.0
    for counter in counters:
        date = counter.get("дата поверки")
        if month1 is not None and date.month == month1:
            month1_total += counter.get("расход", 0.0)
        if month2 is not None and date.month == month2:
            month2_total += counter.get("расход", 0.0)
    return month1_total, month2_total


def find_peak_day(counters):
    peak_counter = None
    peak_day = None
    peak_value = 0.0
    for counter in counters:
        day = counter.get("дата поверки")
        value = counter.get("расход", 0.0)
        if value > peak_value:
            peak_value = value
            peak_counter = counter
            peak_day = day
    return peak_counter, peak_day, peak_value
