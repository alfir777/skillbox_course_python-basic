# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_figure(start_point, side_count, angle, length, color):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3)
        elif side == side_count - 1:
            sd.line(vector.end_point, start_point, color=color)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector.draw(color=color)


def triangle(start_point, angle=0, length=0, color=sd.COLOR_ORANGE):
    side_count = 3
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length, color=color)


def square(start_point, angle=0, length=0, color=sd.COLOR_ORANGE):
    side_count = 4
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length, color=color)


def pentagon(start_point, angle=0, length=0, color=sd.COLOR_ORANGE):
    side_count = 5
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length, color=color)


def hexagon(start_point, angle=0, length=0, color=sd.COLOR_ORANGE):
    side_count = 6
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length, color=color)


figure = {1: 'Треугольник',
          2: 'Квадрат',
          3: 'Пятиугольник',
          4: 'Шестиугольник'
          }

print('Возможные фигуры:')
pprint(figure)
user_input = int(input('Введите желаемую фигуру: '))
while user_input < 1 or user_input > 7:
    print('Вы ввели неправильный цвет!')
    user_input = int(input('Введите желаемую фигуру: '))

sd.resolution = (400, 400)
start_point = sd.get_point(200, 200)

if user_input == 1:
    color = sd.COLOR_RED
    triangle(start_point=start_point, angle=20, length=100, color=color)
elif user_input == 2:
    color = sd.COLOR_ORANGE
    square(start_point=start_point, angle=20, length=100, color=color)
elif user_input == 3:
    color = sd.COLOR_YELLOW
    pentagon(start_point=start_point, angle=20, length=100, color=color)
elif user_input == 4:
    color = sd.COLOR_GREEN
    hexagon(start_point=start_point, angle=20, length=100, color=color)

sd.pause()
