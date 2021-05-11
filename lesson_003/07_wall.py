# -*- coding: utf-8 -*-

# (цикл for)
import time

import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


sd.resolution = (600, 600)

brick_x = 100
brick_y = 50

row = 0
for y in range(0, sd.resolution[1], brick_y):
    row += 1
    for x in range(0, sd.resolution[0], brick_x):
        x0 = x if row % 2 else x + brick_x // 2
        left_bottom = sd.get_point(x0, y)
        right_top = sd.get_point(x0 + brick_x, y + brick_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_ORANGE, width=3)
        time.sleep(0.01)

sd.pause()
