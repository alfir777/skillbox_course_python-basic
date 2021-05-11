# -*- coding: utf-8 -*-

# (цикл for)
import time
import simple_draw as sd


def wall(coord_x=300, coord_y=100, height=201):
    x = 30
    y = 15

    step_y = coord_y

    for _ in range(0, height, y):
        step_x = coord_x
        if (step_y / 5) % 2:
            for _ in range(0, height, x):
                point_x = sd.get_point(step_x, step_y)
                point_y = sd.get_point(x+step_x, y+step_y)
                sd.rectangle(point_x, point_y, color=sd.COLOR_ORANGE, width=3)
                step_x += x
                time.sleep(0.01)
        else:
            for i in range(0, height, x):
                if i > (height - 50):
                    break
                point_x = sd.get_point(step_x+y, step_y)
                point_y = sd.get_point(x+step_x+y, y+step_y)
                sd.rectangle(point_x, point_y, color=sd.COLOR_ORANGE, width=3)
                step_x += x
                time.sleep(0.01)
        step_y += y

def draw_figure(start_point, side_count, angle, length, color):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3, width=3)
        elif side == side_count - 1:
            sd.line(vector.end_point, start_point, color=color, width=3)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length, width=3)
            step += angle_step
        vector.draw(color=color)


def triangle(start_point, angle=0, length=0, color=sd.COLOR_ORANGE):
    side_count = 3
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length, color=color)


def square(start_point, angle=0, length=0, color=sd.COLOR_ORANGE):
    side_count = 4
    draw_figure(start_point=start_point, side_count=side_count, angle=angle, length=length, color=color)