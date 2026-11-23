# === Stage 10: Сортировка записей ===
# Project: WaterMeter
def sort_by_name(records, ascending=True):
    return sorted(records, key=lambda r: r["name"], reverse=not ascending)


def sort_by_created(records, ascending=True):
    return sorted(records, key=lambda r: r["created_at"], reverse=not ascending)


def sort_by_name_then_created(records, ascending=True):
    return sorted(
        records,
        key=lambda r: (r["created_at"], r["name"]),
        reverse=not ascending,
    )


def sort_by_created_then_name(records, ascending=True):
    return sorted(
        records,
        key=lambda r: (r["name"], r["created_at"]),
        reverse=not ascending,
    )


def get_sorted(records, field, ascending=True):
    return sorted(records, key=lambda r: r[field], reverse=not ascending)


def sort_descending(records, field):
    return sorted(records, key=lambda r: r[field], reverse=True)


def sort_ascending(records, field):
    return sorted(records, key=lambda r: r[field], reverse=False)


def sort_name_ascending(records):
    return sorted(records, key=lambda r: r["name"], reverse=False)


def sort_name_descending(records):
    return sorted(records, key=lambda r: r["name"], reverse=True)


def sort_created_ascending(records):
    return sorted(records, key=lambda r: r["created_at"], reverse=False)


def sort_created_descending(records):
    return sorted(records, key=lambda r: r["created_at"], reverse=True)
