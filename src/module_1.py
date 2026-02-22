# Stepick.org — Python в примерах и задачах
# 1. Простые программы на Python, основы вычислений

from math import asin, cos, sqrt, pi

# === 1.1 Задача. "Hello, world!" ===


def m_1_1_1():
    """
    Задача
    -------------------------------------
    Написать программу, которая выводит сообщение "Я изучаю Python!".
    """
    print("Я изучаю Python!")


# === 1.2 Задача. Вычисление индекса массы тела и его интерпретация ===


def m_1_2_1():
    """
    Задача
    -------------------------------------
    Вычислить индекс массы тела в зависимости от роста, веса и возраста,
    а затем проинтерпретировать результат в соответствии с рекомендациями
    Всемирной Организации Здравоохранения.
    """
    age = int(input())
    height = float(input())
    weight = float(input())

    if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
        print("Ошибочные входные данные")
    else:
        bmi = weight / height**2
        bmi = round(bmi, 2)
        descriptions = [
            "недостаточной массой тела.",
            "нормальной массой тела.",
            "избыточной массой тела.",
            "ожирением.",
        ]
        frames = [18.5, 25, 30] if age < 45 else [22, 27, 32]
        for i, b in enumerate(frames):
            if bmi < b:
                res = i
                break
        else:
            res = 3
        description = descriptions[res]
        print("bmi=", bmi, "Вы относитесь к группе людей с", description)


# === 1.3 Задача. Геометрические вычисления на плоскости ===


def m_1_3_1():
    """
    Задача
    -------------------------------------
    Вычислить значение следующего выражения,
    результат округлить до 5 знаков после запятой:
    """
    x, y = float(input()), float(input())
    z = (asin(cos(x + sqrt(3) / 2 * pi)) + 1.2 * sqrt(2 - (cos(y)) ** 2)) / (
        pow(x, 2) + pow(y, 2) + 1
    )
    print(round(z, 5))


def m_1_3_2():
    """
    Задача
    -------------------------------------
    Дан треугольник ABC на плоскости, заданный координатами своих вершин.

    Для этого треугольника вычислить:

        - радиус вписанной в треугольник окружности;
        - радиус описанной вокруг треугольника окружности;
        - сумму длин трех медиан треугольника.
    """

    def side_len(x1, y1, x2, y2):
        sl = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return sl

    def is_real(a, b, c):
        existence = (a + b) > c and (b + c) > a and (c + a) > b
        return existence

    def inscribed(a, b, c):
        p = (a + b + c) / 2
        r = sqrt((p - a) * (p - b) * (p - c) / p)
        return r

    def circumscribed(a, b, c):
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        r = (a * b * c) / (4 * s)
        return r

    def median(a, b, c):
        m = sqrt(2 * (c**2 + b**2) - a**2) / 2
        return m

    def creater():
        a_xy = (float(input()), float(input()))
        b_xy = (float(input()), float(input()))
        c_xy = (float(input()), float(input()))

        a = side_len(*b_xy, *c_xy)
        b = side_len(*a_xy, *c_xy)
        c = side_len(*a_xy, *b_xy)

        return a, b, c

    def main():
        a, b, c = creater()
        if not is_real(a, b, c):
            return ("error",)
        inscrib = round(inscribed(a, b, c), 4)
        circumscrib = round(circumscribed(a, b, c), 4)
        medians = round(median(a, b, c) + median(b, c, a) + median(c, a, b), 4)
        return inscrib, circumscrib, medians

    print(*main())
