# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd


def rainbow(size=1):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step = 900 * size
    center_position = sd.get_point(400 * size, -100 * size,)
    for rainbow_color in rainbow_colors:
        sd.circle(center_position=center_position, radius=step, color=rainbow_color, width=20)
        step += 20 * size
