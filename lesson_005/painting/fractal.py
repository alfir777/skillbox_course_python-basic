# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    delta = 30
    next_length = length * .75
    next_angle = angle - delta
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    next_angle = angle + delta
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)


def draw_branches_v2(start_point, angle, length):
    if length < 15:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    delta = 25
    percent_delta = round(delta * .4)
    delta += sd.random_number(-percent_delta, percent_delta)
    next_length = length * .75
    percent_length = round(next_length * .2)
    next_length += sd.random_number(0, percent_length)
    next_angle = round(angle - delta)
    draw_branches_v2(start_point=next_point, angle=next_angle, length=next_length)
    next_angle = round(angle + delta)
    draw_branches_v2(start_point=next_point, angle=next_angle, length=next_length)


if __name__ == '__main__':
    sd.resolution = (1200, 600)

    root_point = sd.get_point(300, 30)
    draw_branches(start_point=root_point, angle=90, length=100)

    root_point = sd.get_point(900, 30)
    draw_branches_v2(start_point=root_point, angle=90, length=100)


# sd.pause()
