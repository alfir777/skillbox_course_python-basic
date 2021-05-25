# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1200, 800)


class Snowflake:
    down_snowflakes = []

    def __init__(self):
        self.length = sd.random_number(5, 15)
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = 700
        self.factor_a = sd.random_number(1, 10) / 10
        self.factor_b = sd.random_number(1, 10) / 10
        self.factor_c = sd.random_number(10, 120)

    def clear_previous_picture(self):
        self.draw(color=sd.background_color)

    def move(self):
        self.x += sd.random_number(0, 2)
        self.y -= self.length + sd.random_number(-5, 5)

    def draw(self, color=sd.COLOR_WHITE):
        start_point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=start_point,
                     length=self.length,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def can_fall(self):
        if self.y > 0:
            return True


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

def get_flakes(count):
    _flakes = {}
    for i in range(count):
        _flakes[i + 1] = Snowflake()
    return _flakes


N = 20
fallen_flakes = []

flakes = get_flakes(count=N)


def get_fallen_flakes(flakes):
    for number, flake_parameter in flakes.items():
        if flake_parameter.y < 0:
            fallen_flakes.append(number)
    return fallen_flakes


def append_flakes(fallen_flakes=fallen_flakes):
    for fallen in fallen_flakes:
        flakes[fallen] = Snowflake()
    fallen_flakes.clear()
    return fallen_flakes


while True:
    for num, flake in flakes.items():
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        if not flake.can_fall():
            break
    fallen_flakes = get_fallen_flakes(flakes=flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(fallen_flakes=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
