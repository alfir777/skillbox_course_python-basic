# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color=simple_draw.COLOR_ORANGE):

    # голова
    point_head = simple_draw.get_point(x, y)
    radius = 100
    simple_draw.circle(center_position=point_head, color=color, radius=radius)

    # глаза
    point_eye1_1 = simple_draw.get_point(x-50, y)
    radius = 20
    simple_draw.circle(center_position=point_eye1_1, color=color, radius=radius)
    point_eye1_2 = simple_draw.get_point(x-50, y)
    radius = 5
    simple_draw.circle(center_position=point_eye1_2, color=color, radius=radius, width=5)
    point_eye2_1 = simple_draw.get_point(x+50, y)
    radius = 20
    simple_draw.circle(center_position=point_eye2_1, color=color, radius=radius)
    point_eye2_2 = simple_draw.get_point(x+50, y)
    radius = 5
    simple_draw.circle(center_position=point_eye2_2, color=color, radius=radius, width=5)

    # рот
    point_mouth1 = simple_draw.get_point(x-40, y-40)
    point_mouth2 = simple_draw.get_point(x - 30, y - 50)
    point_mouth3 = simple_draw.get_point(x + 30, y - 50)
    point_mouth4 = simple_draw.get_point(x + 40, y - 40)
    simple_draw.line(point_mouth1, point_mouth2, color=color, width=1)
    simple_draw.line(point_mouth2, point_mouth3, color=color, width=1)
    simple_draw.line(point_mouth3, point_mouth4, color=color, width=1)


for _ in range(10):
    x_r = random.randint(50, 550)
    y_r = random.randint(50, 550)
    smile(x=x_r, y=y_r, color=simple_draw.COLOR_CYAN)

simple_draw.pause()
