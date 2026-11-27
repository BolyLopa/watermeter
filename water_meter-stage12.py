# === Stage 12: Теги ===
# Project: WaterMeter
from datetime import datetime


class WaterTag:
    """Метаданные-тег для счётчика воды.

    Хранит название тега и связывает его с одним счётчиком.
    """

    def __init__(self, name, meter_id, meter_name=""):
        self.name = name
        self.meter_id = meter_id
        self.meter_name = meter_name

    def __repr__(self):
        return f"WaterTag(name={self.name!r}, meter_id={self.meter_id!r})"


class MeterTagManager:
    """Управление тегами счётчиков: добавление, удаление, поиск.

    Работает с коллекцией счётчиков (словарь meter_id -> объект счётчика),
    чтобы связывать теги с конкретными устройствами.
    """

    def __init__(self, meters=None):
        self._meters = meters or {}
        self._tags = {}  # tag_name -> WaterTag

    def add_tag(self, tag_name, meter_id, meter_name=""):
        """Добавить тег к счётчику. Возвращает WaterTag или None."""
        if not tag_name or not meter_id:
            return None
        if meter_id in self._meters:
            meter_name = getattr(self._meters[meter_id], "name", meter_name)
        tag = WaterTag(tag_name, meter_id, meter_name)
        self._tags[tag_name] = tag
        return tag

    def remove_tag(self, tag_name):
        """Удалить тег по имени. Возвращает WaterTag или None."""
        tag = self._tags.pop(tag_name, None)
        if tag is not None:
            self._meters.get(tag.meter_id, None)
        return tag

    def find_by_tag(self, tag_name):
        """Найти счётчик по тегу. Возвращает meter_id или None."""
        tag = self._tags.get(tag_name)
        return tag.meter_id if tag else None

    def list_meter_tags(self, meter_id):
        """Собрать все теги для указанного счётчика."""
        result = []
        for tag in self._tags.values():
            if tag.meter_id == meter_id:
                result.append(tag)
        return result

    def list_all_tags(self):
        """Собрать все существующие теги."""
        return list(self._tags.values())
