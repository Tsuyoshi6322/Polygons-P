import math
from .file_management import *
from .polygon_definition import *
from .output_messages import *


# Calculate the area of the polygon
def polygon_calculate_area(file_path, polygon_defined, epsilon):
    output_message("status", "Calculating the area of the polygon")

    points, _ = data_file_import(file_path)

    point_a = points.get("A")
    point_b = points.get("B")
    point_c = points.get("C")
    point_d = points.get("D")

    # Length of the sides of the polygon
    AB = polygon_distance(point_a, point_b)
    BC = polygon_distance(point_b, point_c)
    CA = polygon_distance(point_c, point_a)
    if point_d is not None:
        CD = polygon_distance(point_c, point_d)

    if polygon_defined == "Equilateral triangle" or "Right triangle" or "Isosceles triangle" or "Scalene triangle":
        half_perimeter = round((AB + BC + CA) / 2, 2)
        area_calculated = math.sqrt(half_perimeter * (half_perimeter - AB) * (half_perimeter - BC) * (half_perimeter - CA))

    elif polygon_defined == "Square":
        area_calculated = round(AB ** 2, 2)

    elif polygon_defined == "Rectangle":
        area_calculated = round(AB * BC, 2)

    elif polygon_defined == "Trapezoid":
        base_a = AB
        base_b = CD
        height = polygon_distance(point_b, point_d)
        area_calculated = round((base_a + base_b) * height / 2, 2)
    else:
        output_message("error", "Could not calculate the area of the polygon")

    return area_calculated


# Calculate the perimeter of the polygon
def polygon_calculate_perimeter(file_path, polygon_defined, epsilon):
    output_message("status", "Calculating the perimeter of the polygon")

    points, pointsCount = data_file_import(file_path)

    labels = ["A", "B", "C", "D"]

    # For triangles
    if pointsCount == 6:
        perimeter_calculated = sum(polygon_distance(points[labels[i]], points[labels[(i+1)%3]]) for i in range(3))

    # For quadrilaterals
    elif pointsCount == 8:
        perimeter_calculated = sum(polygon_distance(points[labels[i]], points[labels[(i+1)%4]]) for i in range(4))

    else:
        output_message("error", "Unknown type of figure or incorrect number of points.")

    return perimeter_calculated


# Export the results
def polygon_calculate_main(file_path, epsilon):
    polygon_defined = polygon_define_main(file_path, epsilon)

    area_calculated = polygon_calculate_area(file_path, polygon_defined, epsilon)
    output_message("ok", "Area calculated successfully")

    perimeter_calculated = polygon_calculate_perimeter(file_path, polygon_defined, epsilon)
    output_message("ok", "Perimeter calculated successfully")

    data_file_export(file_path, area_calculated)
    data_file_export(file_path, perimeter_calculated)
