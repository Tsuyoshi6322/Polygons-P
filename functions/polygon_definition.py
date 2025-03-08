import math
from .file_management import *
from .output_messages import *

# Are the points collinear?
def polygon_are_collinear(p1, p2, p3, p4=None):
    output_message("status", "Checking if the points are collinear")

    collinear = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    return collinear

# Defining the polygon
def polygon_calculate_points(file_path):
    points, pointsCount = data_file_import(file_path)

    # Checking if the points are correct - should the program flip out
    if pointsCount == 6 or pointsCount == 8:
        point_a = points.get("A")
        point_b = points.get("B")
        point_c = points.get("C")
        point_d = points.get("D")

    else:
        output_message("error", "Polygon is out of scope")


    # In case of triangles
    if point_d is None:
        collinear = polygon_are_collinear(point_a, point_b, point_c)

    # In case of quadrilaterals
    else:
        collinear = polygon_are_collinear(point_a, point_b, point_c)
        + polygon_are_collinear(point_a, point_b, point_d)
        + polygon_are_collinear(point_a, point_c, point_d)
        + polygon_are_collinear(point_b, point_c, point_d)


    # If the points are collinear, the program will exit as they do not form a polygon
    if collinear == 0:
        output_message("error", "The points do not form a polygon")

    else:
        if pointsCount == 6:
            polygon = "triangle"

        elif pointsCount == 8:
            polygon = "quadrilateral"

        else:
            output_message("error", "Polygon out of scope")

    return polygon


# Calculate the distance between two points
def polygon_distance(p1,p2):
    output_message("status", "Calculating the distance between two points")

    return math.dist((p1.x, p1.y), (p2.x, p2.y))


# Define the type of triangle
def polygon_is_triangle(file_path, epsilon):
    output_message("ok", "The polygon is a triangle")
    output_message("status", "Determining the type of the triangle")

    points, _ = data_file_import(file_path)

    point_a = points.get("A")
    point_b = points.get("B")
    point_c = points.get("C")

    # Distances between points
    AB = polygon_distance(point_a, point_b)
    BC = polygon_distance(point_b, point_c)
    CA = polygon_distance(point_c, point_a)

    # Checking the type of triangle with approximations
    if math.isclose(AB, BC, rel_tol=epsilon) and math.isclose(BC, CA, rel_tol=epsilon):
        output_message("ok", "The polygon is an equilateral triangle")
        polygon_defined = "Equilateral triangle"

    elif math.isclose(AB**2 + BC**2, CA**2) or math.isclose(AB**2 + CA**2, BC**2) or math.isclose(BC**2 + CA**2, AB**2):
        output_message("ok", "The polygon is a right triangle")
        polygon_defined = "Right triangle"

    elif AB == BC or AB == CA or BC == CA:
        output_message("ok", "The polygon is an isosceles triangle")
        polygon_defined = "Isosceles triangle"

    else:
        output_message("ok", "The polygon is an scalene triangle")
        polygon_defined = "Scalene triangle"

    return polygon_defined


# Determine the type of quadrilateral
def polygon_is_quadrilateral(file_path, epsilon):
    output_message("status", "The polygon is a quadrilateral")
    output_message("status", "Determining the type of the quadrilateral")

    points, _ = data_file_import(file_path)

    point_a = points.get("A")
    point_b = points.get("B")
    point_c = points.get("C")
    point_d = points.get("D")

    # Calculating the length of the sides
    AB = polygon_distance(point_a, point_b)
    BC = polygon_distance(point_b, point_c)
    CD = polygon_distance(point_c, point_d)
    DA = polygon_distance(point_d, point_a)

    # Calculating the length of the diagonals
    AC = polygon_distance(point_a, point_c)
    BD = polygon_distance(point_b, point_d)

    # Is it a square?
    if math.isclose(AB, BC, rel_tol=epsilon) and \
          math.isclose(BC, CD, rel_tol=epsilon) and \
          math.isclose(CD, DA, rel_tol=epsilon):
        output_message("ok", "The polygon is a square")
        polygon_defined = "Square"

    # Is it a rectangle?
    elif (math.isclose(AB, CD, rel_tol=epsilon) and math.isclose(BC, DA, rel_tol=epsilon)) and \
         math.isclose(AC, BD, rel_tol=epsilon):
        output_message("ok", "The polygon is a rectangle")
        polygon_defined = "Rectangle"

    # Is it a trapezoid?
    elif (math.isclose(AB, CD, rel_tol=epsilon) and math.isclose(BC, DA, rel_tol=epsilon)) or \
         (math.isclose(AB, DA, rel_tol=epsilon) and math.isclose(BC, CD, rel_tol=epsilon)):
        output_message("ok", "The polygon is a trapezoid")
        polygon_defined = "Trapezoid"

    else:
        output_message("error", "The quadrilateral is out of scope")

    return polygon_defined


# Results to file
def polygon_define_main(file_path, epsilon):
    output_message("status", "Defining the polygon")

    polygon = polygon_calculate_points(file_path)

    if polygon == "triangle":
        polygon_defined = polygon_is_triangle(file_path, epsilon)

    elif polygon == "quadrilateral":
        polygon_defined = polygon_is_quadrilateral(file_path, epsilon)

    # Does the polygon type exist in the file?
    with open(file_path, "r") as file:
        output_message("status", "Reading file contents")
        content = file.read().strip()

    # If not, write the results to the file
    if polygon_defined not in content:
        output_message("status", "Writing the results to file")
        data_file_export(file_path, polygon_defined)
