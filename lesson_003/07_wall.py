# -*- coding: utf-8 -*-

# (цикл for)
import time

import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


sd.resolution = (600, 600)
x = 100
y = 50

step_y = 0

for _ in range(0, 601, y):
    step_x = 0
    if (step_y / 10) % 2:
        for _ in range(0, 601, x):
            point_x = sd.get_point(step_x, step_y)
            point_y = sd.get_point(x+step_x, y+step_y)
            sd.rectangle(point_x, point_y, color=sd.COLOR_ORANGE, width=3)
            step_x += x
            time.sleep(0.01)
    else:
        for _ in range(0, 601, x):
            point_x = sd.get_point(step_x+y, step_y)
            point_y = sd.get_point(x+step_x+y, y+step_y)
            sd.rectangle(point_x, point_y, color=sd.COLOR_ORANGE, width=3)
            step_x += x
            time.sleep(0.01)
    step_y += y

sd.pause()
