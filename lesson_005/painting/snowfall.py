# -*- coding: utf-8 -*-

import simple_draw as sd


def snowfall():
    count_snowfall = 20

    x = []
    for _ in range(count_snowfall):
        x.append(sd.random_number(50, 1150))
    y = []
    for _ in range(count_snowfall):
        y.append(sd.random_number(100, 550))

    while True:
        sd.start_drawing()
        for i in range(len(x)):
            if i > 0:
                point1 = sd.get_point(x[i-1], y[i-1])
                sd.snowflake(center=point1, length=50, color=sd.COLOR_WHITE)
            point = sd.get_point(x[i], y[i])
            if y[i] > 50:
                sd.snowflake(center=point, length=50, color=sd.background_color)
                y[i] -= sd.random_number(-1, 15)
                x[i] = x[i] + sd.random_number(-15, 15)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

