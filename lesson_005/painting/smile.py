# -*- coding: utf-8 -*-

import simple_draw


def smile(x, y, size=1, color=simple_draw.COLOR_ORANGE):

    # голова
    point_head = simple_draw.get_point(x, y)
    radius = 80 * size
    simple_draw.circle(center_position=point_head, color=color, radius=radius)

    # глаза
    point_eye1_1 = simple_draw.get_point(x - 35 * size, y)
    radius = 20 * size
    simple_draw.circle(center_position=point_eye1_1, color=color, radius=radius)
    point_eye1_2 = simple_draw.get_point(x - 35 * size, y)
    radius = 5 * size
    simple_draw.circle(center_position=point_eye1_2, color=color, radius=radius, width=5)
    point_eye2_1 = simple_draw.get_point(x + 35 * size, y)
    radius = 20 * size
    simple_draw.circle(center_position=point_eye2_1, color=color, radius=radius)
    point_eye2_2 = simple_draw.get_point(x + 35 * size, y)
    radius = 5 * size
    simple_draw.circle(center_position=point_eye2_2, color=color, radius=radius, width=5)

    # рот
    point_mouth1 = simple_draw.get_point(x - 40 * size, y - 40 * size)
    point_mouth2 = simple_draw.get_point(x - 30 * size, y - 50 * size)
    point_mouth3 = simple_draw.get_point(x + 30 * size, y - 50 * size)
    point_mouth4 = simple_draw.get_point(x + 40 * size, y - 40 * size)
    simple_draw.line(point_mouth1, point_mouth2, color=color, width=1)
    simple_draw.line(point_mouth2, point_mouth3, color=color, width=1)
    simple_draw.line(point_mouth3, point_mouth4, color=color, width=1)
