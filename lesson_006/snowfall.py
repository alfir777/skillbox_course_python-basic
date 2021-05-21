# -*- coding: utf-8 -*-

import simple_draw as sd


def create_snowflakes(count_snowflakes=20):
    y = 500
    new_snowflakes = {}
    for i in range(count_snowflakes):
        new_snowflakes[i] = {'length': sd.random_number(5, 15),
                             'x': sd.random_number(0, sd.resolution[0]),
                             'y': y,
                             'factor_a': sd.random_number(1, 10) / 10,
                             'factor_b': sd.random_number(1, 10) / 10,
                             'factor_c': sd.random_number(10, 120)}
    return new_snowflakes


def draw_snowflakes_color(center, color=sd.background_color):
    sd.snowflake(center=center,
                 length=snowflakes_v['length'],
                 color=color,
                 factor_a=snowflakes_v['factor_a'],
                 factor_b=snowflakes_v['factor_b'],
                 factor_c=snowflakes_v['factor_c'])


def move_snowflakes(snowflake):
    snowflake['x'] += sd.random_number(-5, 5)
    snowflake['y'] -= snowflake['length']
    point = sd.get_point(snowflake['x'], snowflake['y'])
    return point


def numbers_reached_down_screen(snowflake):
    if snowflakes_v['y'] < 50:
        snowflakes_v['y'] = y
        snowflakes_v['x'] = sd.random_number(0, sd.resolution[0])
    return snowflakes_k


def delete_snowflakes(numbers):
    for i in numbers:
        snowflakes.pop(i)
    numbers_reached.clear()


numbers_reached = []

if __name__ == "__main__":
    sd.resolution = (1200, 600)
    y = 500
    snowflakes = create_snowflakes(count_snowflakes=20)

    while True:
        sd.start_drawing()
        for snowflakes_k, snowflakes_v in snowflakes.items():
            start_point = sd.get_point(snowflakes_v['x'], snowflakes_v['y'])
            draw_snowflakes_color(center=start_point, color=sd.background_color)

            next_point = move_snowflakes(snowflake=snowflakes_v)
            draw_snowflakes_color(center=next_point, color=sd.COLOR_WHITE)

            numbers_reached.append(numbers_reached_down_screen(snowflake=snowflakes_k))
            # delete_snowflakes(numbers_reached)

        # if len(numbers_reached) > 0:
        #     delete_snowflakes(numbers=numbers_reached)
        #     create_snowflakes(count_snowflakes=len(numbers_reached))

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

    sd.pause()
