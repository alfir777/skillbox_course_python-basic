# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_figure(start_point, side_count, angle, length):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length+3)
        elif side == side_count-1:
            sd.line(vector.end_point, start_point)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector.draw()


def triangle(start_point, angle=0, length=0):
    side_count = 3
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length)


def square(start_point, angle=0, length=0):
    side_count = 4
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length)


def pentagon(start_point, angle=0, length=0):
    side_count = 5
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length)


def hexagon(start_point, angle=0, length=0):
    side_count = 6
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length)


sd.resolution = (800, 800)

start_point = sd.get_point(150, 600)
triangle(start_point=start_point, angle=20, length=100)

start_point = sd.get_point(500, 600)
square(start_point=start_point, angle=20, length=100)

start_point = sd.get_point(200, 200)
pentagon(start_point=start_point, angle=20, length=100)

start_point = sd.get_point(600, 100)
hexagon(start_point=start_point, angle=20, length=100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
