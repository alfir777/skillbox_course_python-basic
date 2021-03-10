# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# step = 0
# for rainbow_color in rainbow_colors:
#     point_x = sd.get_point(50 + step, 50)
#     point_y = sd.get_point(350 + step, 450)
#     sd.line(point_x, point_y, rainbow_color, width=4)
#     step += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
step = 150
center_position = sd.get_point(300, 0)
for rainbow_color in rainbow_colors:
    sd.circle(center_position=center_position, radius=step, color=rainbow_color, width=20)
    step += 20

sd.pause()
