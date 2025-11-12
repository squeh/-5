import math


def calculate_distance  (x1, y1, x2, y2):
    '''
    Вычисляет евклидово расстояние между двумя точками.
    
    Args:
        x1, y1 (float): Координаты первой точки.
        x2, y2 (float): Координаты второй точки.
        
    Returns:
        float: Расстояние между точками.
    '''

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def calculate_triangle_area(distance_a, distance_b, distance_c):
    '''
    Принимает на вход длины трех сторон и вычисляет площадь по формуле Герона

    Args:
        distance_a (float): Сторона А
        distance_b (float): Сторона B
        distance_c (float): Сторона C

    Returns:
        float: Длина трех сторон
    '''
    s_triangle = distance_a * distance_b * distance_c
    return s_triangle

x1, y1, x2, y2 = map(float, input().split())
distance_a = calculate_distance(x1, y1, x2, y2)

x2, y2, x3, y3 = map(float, input().split())
distance_b = calculate_distance(x2, y2, x3, y3)

x3, y3, x1, y1 = map(float, input().split())
distance_c = calculate_distance(x3, y3, x1, y1)

print(f" Площадь треугольника равна {calculate_triangle_area(distance_a, distance_b, distance_c)}")
