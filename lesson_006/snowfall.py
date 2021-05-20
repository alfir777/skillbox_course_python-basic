# -*- coding: utf-8 -*-

import simple_draw as sd


def create_snowflakes(count_snowflakes=20):
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


def nudge_snowflakes():
    #  сдвинуть_снежинки() - сдвигает снежинки на один шаг
    pass


def numbers_reached_down_screen():
    #  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
    pass


def delete_snowflakes(numbers):
    #  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
    pass


sd.resolution = (1200, 600)
y = 500
snowflakes = create_snowflakes(count_snowflakes=20)

while True:
    sd.start_drawing()
    for snowflakes_k, snowflakes_v in snowflakes.items():
        start_point = sd.get_point(snowflakes_v['x'], snowflakes_v['y'])
        draw_snowflakes_color(center=start_point, color=sd.background_color)

        snowflakes_v['x'] += sd.random_number(-5, 5)
        snowflakes_v['y'] -= snowflakes_v['length']

        next_point = sd.get_point(snowflakes_v['x'], snowflakes_v['y'])
        draw_snowflakes_color(center=next_point, color=sd.COLOR_WHITE)

        if snowflakes_v['y'] < 50:
            snowflakes_v['y'] = y
            snowflakes_v['x'] = sd.random_number(0, sd.resolution[0])

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
