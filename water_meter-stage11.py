# === Stage 11: Поиск по нескольким словам ===
# Project: WaterMeter
from typing import Iterable, Iterator


def _split_query(query: str) -> list[str]:
    """Разбивает строку запроса на токены, отбрасывая пустые."""
    return [token for token in query.replace("-", " - ").split() if token.strip()]


def _matches_all(tokens: list[str], counter_name: str) -> bool:
    """Проверяет, что все слова (кроме исключений) встречаются в названии."""
    required = [t for t in tokens if not t.startswith("-")]
    excluded = [t.lstrip("-") for t in tokens if t.startswith("-")]

    if not required:
        return True

    name_tokens = set(token.lower() for token in counter_name.split())
    matched = {token.lower() for token in required if token.lower() in name_tokens}

    return required and matched == required and not excluded


def search_counters(query: str, counters: Iterable[str]) -> Iterator[str]:
    """Ищет счётчики по нескольким словам с поддержкой исключений.

    Поиск ищет совпадение всех обязательных слов в названии счётчика.
    Слова с префиксом '-' исключают совпадения по соответствующему слову.
    """
    tokens = _split_query(query)
    required = [t for t in tokens if not t.startswith("-")]
    excluded = [t.lstrip("-") for t in tokens if t.startswith("-")]

    for counter_name in counters:
        if not required:
            yield counter_name
            continue

        name_tokens = {token.lower() for token in counter_name.split()}
        matched = {token.lower() for token in required if token.lower() in name_tokens}

        if required and matched == required and not any(
            excluded_word in name_tokens for excluded_word in excluded
        ):
            yield counter_name


if __name__ == "__main__":
    data = [
        "Домашний счётчик",
        "Тепловой узел",
        "Канализация",
        "Уличный счётчик",
    ]

    print(search_counters("домашний", data))
    print(search_counters("счётчик -канализация", data))
    print(search_counters("домашний -тепловой", data))
    print(search_counters("домашний -тепловой -уличный", data))
