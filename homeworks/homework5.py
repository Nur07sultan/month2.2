from homeworks.distance import Distance

# Основные проверки
a = Distance(100, "m")
b = Distance(1, "km")
c = Distance(50, "cm")

print(a, "+", b, "=", a + b)       # 100 м + 1 км
print(b, "-", a, "=", b - a)       # 1 км - 100 м
print("Сравнение:", a, "<", b, "?", a < b)
print("Сравнение:", a, "==", Distance(100, "m"), "?", a == Distance(100, "m"))
print("Сравнение:", c, "<", a, "?", c < a)

# -----------------------------
# Доп. задание: список расстояний
# -----------------------------
distances = [
    Distance(500, "m"),
    Distance(2, "km"),
    Distance(150, "cm"),
    Distance(50, "m"),
]

print("\nИсходный список:")
for d in distances:
    print(d)

print("\nСортировка по величине:")
for d in sorted(distances):
    print(d)

print("\nМаксимальное расстояние:", max(distances))
print("Минимальное расстояние:", min(distances))