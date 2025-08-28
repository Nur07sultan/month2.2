class Distance:
    """
    Класс для работы с расстояниями.
    Поддерживает сложение, вычитание (без отрицательных значений)
    и сравнение (учитывая разные единицы измерения).
    """

    UNIT_CONVERSIONS = {
        "m": 1,       # метры
        "km": 1000,   # километры
        "cm": 0.01,   # сантиметры
    }

    def __init__(self, value, unit="m"):
        if unit not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Неизвестная единица измерения: {unit}")
        if value < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self.value = value
        self.unit = unit

    def to_meters(self):
        """Переводит значение в метры"""
        return self.value * self.UNIT_CONVERSIONS[self.unit]

    def __str__(self):
        return f"{self.value} {self.unit}"

    # Арифметика
    def __add__(self, other):
        total_m = self.to_meters() + other.to_meters()
        return Distance(total_m, "m")

    def __sub__(self, other):
        diff_m = self.to_meters() - other.to_meters()
        if diff_m < 0:
            raise ValueError("Результат не может быть отрицательным!")
        return Distance(diff_m, "m")

    # Сравнения
    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()