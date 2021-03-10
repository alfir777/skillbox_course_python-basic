# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# TODO  в процессе

sd.resolution = (1200, 600)
x = 100
y = 50

x_count = sd.resolution[0] // x
y_count = sd.resolution[1] // y
step = x
for line in range(x_count, x):
    point_x = sd.get_point(50 + step, 50)
    point_y = sd.get_point(350 + step, 450)
    sd.line(point_x, point_y, color=sd.COLOR_ORANGE, width=4)
    step += 5

sd.pause()
