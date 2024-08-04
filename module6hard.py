import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        self.__sides = sides
        self.__color = [*color]
        self.filled = filled

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            pass

    def __is_valid_color(self, r, g, b):
        return (
                isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255
        )

    def __is_valid_sides(self, *new_sides):
        return (
                len(new_sides) == len(self.__sides) and
                all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, circumference, color, filled=True):
        super().__init__([circumference], color, filled)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=True):
        if len(sides) != 3:
            raise ValueError("Треугольник имеет 3 стороны!")
        super().__init__(sides, color, filled)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона
        height = (2 * area) / a  # Высота, опущенная на сторону a
        return height

    def get_height(self):
        return self.__height

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, side_length, color, filled=True):
        sides = [side_length] * self.sides_count
        super().__init__(sides, color, filled)
        self.__side_length = side_length

    def get_volume(self):
        return self.__side_length ** 3


circle1 = Circle(10, (200, 200, 100))  # (Цвет, стороны)
cube1 = Cube(6, (222, 35, 130))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
