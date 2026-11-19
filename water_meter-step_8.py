# === Stage 8: Генерация идентификаторов ===
# Project: WaterMeter
import uuid


PROJECT_PREFIX = "wm"


def generate_id() -> str:
    """Генерация уникального идентификатора с префиксом проекта."""
    return f"{PROJECT_PREFIX}-{uuid.uuid4().hex}"


def is_unique_id(candidates: set, new_id: str) -> bool:
    """Проверка уникальности идентификатора среди уже существующих."""
    return new_id not in candidates


def generate_unique_id(candidates: set) -> str:
    """Генерация идентификатора с проверкой коллизий.

    Генерирует уникальный идентификатор с префиксом проекта и
    проверяет его на отсутствие коллизий в переданном наборе.
    При коллизии генерирует новый идентификатор и повторяет проверку.
    """
    new_id = generate_id()
    while not is_unique_id(candidates, new_id):
        new_id = generate_id()
    return new_id
