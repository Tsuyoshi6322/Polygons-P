import math
from .file_management import *
from .polygon_definition import *
from .output_messages import *

# =============== OBLICZENIE POLA I OBWODU FIGURY ===============
# Obliczenie pola figury
def polygon_calculate_area(file_path, polygon_defined, epsilon):
    points, _ = data_file_import(file_path)

    point_a = points.get("A")
    point_b = points.get("B")
    point_c = points.get("C")
    point_d = points.get("D")

    # Długości boków
    AB = polygon_distance(point_a, point_b)
    BC = polygon_distance(point_b, point_c)
    CA = polygon_distance(point_c, point_a)
    if point_d is not None:
        CD = polygon_distance(point_c, point_d)

    if polygon_defined == "Trojkat Rownoboczny" or "Trojkat Prostokatny" or "Trojkat Rownoramienny" or "Trojkat Roznoboczny":
        half_perimeter = round((AB + BC + CA) / 2, 2)
        area_calculated = math.sqrt(half_perimeter * (half_perimeter - AB) * (half_perimeter - BC) * (half_perimeter - CA))

    elif polygon_defined == "Kwadrat":
        area_calculated = round(AB ** 2, 2)

    elif polygon_defined == "Prostokąt":
        area_calculated = round(AB * BC, 2)

    elif polygon_defined == "Trapez":
        base_a = AB
        base_b = CD
        height = polygon_distance(point_b, point_d)
        area_calculated = round((base_a + base_b) * height / 2, 2)
    else:
        print("Error: Nie udało się obliczyć pola figury")
        exit()

    return area_calculated

# Obliczenie obwodu figury
def polygon_calculate_perimeter(file_path, polygon_defined, epsilon):
    points, pointsCount = data_file_import(file_path)

    labels = ["A", "B", "C", "D"]

    if pointsCount == 6: # Dla trójkątów
        perimeter_calculated = sum(polygon_distance(points[labels[i]], points[labels[(i+1)%3]]) for i in range(3))

    elif pointsCount == 8: # Dla czworokątów
        perimeter_calculated = sum(polygon_distance(points[labels[i]], points[labels[(i+1)%4]]) for i in range(4))

    else:
        print("Error: Nieznany typ figury lub nieprawidłowa liczba punktów.")
        exit()

    return perimeter_calculated

# Wynik - eksport do pliku
def polygon_calculate_main(file_path, epsilon):
    polygon_defined = polygon_define_main(file_path, epsilon)

    area_calculated = polygon_calculate_area(file_path, polygon_defined, epsilon)
    perimeter_calculated = polygon_calculate_perimeter(file_path, polygon_defined, epsilon)

    # Eksport wyników do pliku
    data_file_export(file_path, area_calculated)
    data_file_export(file_path, perimeter_calculated)
