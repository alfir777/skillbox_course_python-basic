# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(point, angle, length):
        side_count = n
        vector = point
        angle_step = 360 / side_count
        step = angle_step
        for side in range(side_count):
            if side == 0:
                vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3)
            elif side == side_count - 1:
                sd.line(vector.end_point, point)
                break
            else:
                vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
                step += angle_step
            vector.draw()
    return draw_figure


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
