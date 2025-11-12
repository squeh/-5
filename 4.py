import math

def calculate_rectangle_area(width, height):
  """
  Принимает ширину и высоту и возращает площадь прямоугольника

  Args:
    width, height (float): размеры прямоузольнuка

  Returns:
    float: радиус прямоугольника
  """
  area = width * height
  return area

def calculate_circle_area(radius):
  """
  Вычисляет радиус круга
  Args:
    radius (float): радиус прямоугольника
  Returns:
    float: радиус прямоугольника
    """
  area = 2 * math.pi * radius
  return area

weight, height = map(float, input("Введите высоту и ширину прямоугольника через пробел: ").split())
print(calculate_rectangle_area(weight, height))

radius = float(input("Введите радиус круга: "))
print(calculate_circle_area(radius))
