# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd


def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step = 850
    center_position = sd.get_point(400, 0)
    for rainbow_color in rainbow_colors:
        sd.circle(center_position=center_position, radius=step, color=rainbow_color, width=20)
        step += 20
