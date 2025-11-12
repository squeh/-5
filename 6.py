import math


def calculate_distance  (x1, y1, x2, y2):

    side_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return side_length

def calculate_triangle_area(side_length_a, side_length_b, side_length_c):
    s_triangle = side_length_a * side_length_b * side_length_c
    return s_triangle

x1, y1, x2, y2 = map(float, input().split())
side_length_a = calculate_distance(x1, y1, x2, y2)

x2, y2, x3, y3 = map(float, input().split())
side_length_b = calculate_distance(x2, y2, x3, y3)

x3, y3, x1, y1 = map(float, input().split())
side_length_c = calculate_distance(x3, y3, x1, y1)

print(f" Площадь треугольника равна {calculate_triangle_area(side_length_a, side_length_b, side_length_c)}")
