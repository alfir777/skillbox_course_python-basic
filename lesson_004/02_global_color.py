# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


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


color = {1: 'COLOR_RED',
         2: 'COLOR_ORANGE',
         3: 'COLOR_YELLOW',
         4: 'COLOR_GREEN',
         5: 'COLOR_CYAN',
         6: 'COLOR_BLUE',
         7: 'COLOR_PURPLE'
         }

print('Возможные цвета:')
pprint(color)
user_input = int(input('Введите желаемый цвет: '))
while user_input < 1 or user_input > 7:
    print('Вы ввели неправильный цвет!')
    user_input = int(input('Введите желаемый цвет: '))

if user_input == 1:
    color = sd.COLOR_RED
elif user_input ==  2:
    color = sd.COLOR_ORANGE
elif user_input == 3:
    color = sd.COLOR_YELLOW
elif user_input == 4:
    color = sd.COLOR_GREEN
elif user_input == 5:
    color = sd.COLOR_CYAN
elif user_input == 6:
    color = sd.COLOR_BLUE
elif user_input == 7:
    color = sd.COLOR_PURPLE

sd.resolution = (800, 800)

start_point = sd.get_point(150, 600)
triangle(start_point=start_point, angle=20, length=100, color=color)

start_point = sd.get_point(500, 600)
square(start_point=start_point, angle=20, length=100, color=color)

start_point = sd.get_point(200, 200)
pentagon(start_point=start_point, angle=20, length=100, color=color)

start_point = sd.get_point(600, 100)
hexagon(start_point=start_point, angle=20, length=100, color=color)

sd.pause()
